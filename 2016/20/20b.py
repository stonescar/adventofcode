bl = []
with open("20.txt", "r") as f:
	for line in f.readlines():
		a, b = (line.strip().split("-"))
		bl.append([int(a), int(b)])
bl = sorted(bl)

last = 0
total = 0


for l in bl:
	if l[0] > last + 1:
		total += l[0] - last - 1
	last = max(last, l[1])

print "Total:", total