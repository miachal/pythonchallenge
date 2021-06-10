import requests
from PIL import Image
from io import BytesIO
import re

req = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
img = Image.open(BytesIO(req.content))

width, height = img.size
print('W: {}, H: {}'.format(width, height))

start_x, start_y = (0, 45)
end_x, end_y = (605, 50)
box_cords = (start_x, start_y, end_x, end_y)

box = img.crop(box_cords)
px_map = box.load()

char_width = 7
chars = []
for j in range(0, end_x, char_width):
    chars.append(chr(px_map[j,0][0]))

msg = ''.join(chars)
print(msg)

next_list = re.search(r'\[(.+)\]', msg).group(1).split(', ')

next_level = [chr(i) for i in list(map(int, next_list))]
print('http://pythonchallenge.com/pc/def/{}.html'.format(''.join(next_level)))
