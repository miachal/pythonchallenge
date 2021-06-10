txt = open('0x03.txt').read()

letters = {}

for c in txt:
    letters[c] = letters.get(c, 0) + 1


rare = [k for k, v in letters.items() if v < 10]

print('http://pythonchallenge.com/pc/def/{}.html'.format(''.join(rare)))