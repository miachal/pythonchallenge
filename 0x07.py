import requests
import zipfile
from io import BytesIO
from tempfile import TemporaryDirectory
import re

zip_url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
r = requests.get(zip_url)

ids = []

def go(dir, id):
    ids.append(id)
    with open('{}/{}.txt'.format(dir, id)) as f:
        msg = f.read()
        next = re.search(r'Next nothing is (\d+)', msg)

        if next:
            return go(dir, next.group(1))



with TemporaryDirectory() as tmp_dir:
    with zipfile.ZipFile(BytesIO(r.content)) as package:
        package.extractall(tmp_dir)

        go(tmp_dir, 90052)
        
        for comment in ids:
            zip_info = package.getinfo('{}.txt'.format(comment))
            print(zip_info.comment.decode('utf-8'), end='')
