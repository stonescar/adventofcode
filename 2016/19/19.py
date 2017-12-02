x = 3014603
elfs = []

for i in range(x):
	elfs.append(i+1)


while len(elfs) > 1:
	odd = True if len(elfs) % 2 == 1 else False
	for e in range(len(elfs)):
		if len(elfs)-1 == e and odd:
			del elfs[0]
			break
		elif len(elfs) == e and not odd:
			break
		else:
			del elfs[e+1]
		
print elfs