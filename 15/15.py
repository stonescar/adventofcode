discs = [2, 7, 10, 2, 9, 0, 0]
pos = [5, 13, 17, 3, 19, 7, 11]

for i in range(len(discs)):
	discs[i] = (discs[i]+i+1)%pos[i]
	
count = 0
while True:
	open = True
	for d in discs:
		if d != 0:
			open = False
	if open:
		break
	for i in range(len(discs)):
		discs[i] = (discs[i]+1)%pos[i]
	count += 1
	
print count