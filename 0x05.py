import re
import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

def hop(id):
	r = requests.get(url+str(id))
	next = re.search(r'next nothing is (\d+)', r.text)

	if next:
		hop(next.group(1))
	else:
		if(r.text == 'Yes. Divide by two and keep going.'):
			hop(int(id)/2)
		else:
			print('http://pythonchallenge.com/pc/def/{}'.format(r.text))


print('It can take a while. There is 251 links...')
hop(12345)