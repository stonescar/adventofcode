count = 0
with open("03.txt", "r") as f:
	for line in f.readlines():
		sides = line.split(" ")
		while "" in sides:
			sides.remove("")
		sides[0] = int(sides[0])
		sides[1] = int(sides[1])
		sides[2] = int(sides[2].rstrip())
		sides = sorted(sides, reverse=True)
		if sides[0] < sides[1]+sides[2]:
			count += 1
print count