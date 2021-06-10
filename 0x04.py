import re

txt = open('0x04.txt').read()

lst = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', txt)

print('http://pythonchallenge.com/pc/def/{}.html'.format(''.join(lst)))