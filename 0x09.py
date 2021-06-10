import bz2
import requests
import re

r = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
src = r.text

un = re.search(r'un: \'(.+)\'', src).group(1)
pw = re.search(r'pw: \'(.+)\'', src).group(1)

print('login: {}'.format(bz2.decompress(un.decode('string_escape'))))
print('password: {}'.format(bz2.decompress(pw.decode('string_escape'))))
