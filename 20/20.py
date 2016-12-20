bl = []
with open("20.txt", "r") as f:
	for line in f.readlines():
		a, b = (line.strip().split("-"))
		bl.append([int(a), int(b)])
bl = sorted(bl)

first = 0
for l in bl:
	if l[0] > first + 1:
		print first + 1
		break
	first = max(first, l[1])