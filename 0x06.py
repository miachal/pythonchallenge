import pickle

with open('0x06.p', 'rb') as f:
	data = pickle.load(f)

for lst in data:
	for tup in lst:
		for i in range(tup[1]):
			print(tup[0], end='') 
	print()