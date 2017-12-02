count = 1
new = [[], [], []]
triangles = 0

with open("03.txt", "r") as f:
	for line in f.readlines():
		sides = line.split(" ")
		while "" in sides:
			sides.remove("")
		sides[0] = int(sides[0])
		sides[1] = int(sides[1])
		sides[2] = int(sides[2].rstrip())
		
		for i in range(3):
			if count %3 == 1:
				new[i].append([sides[i]])
			else:
				new[i][len(new[i])-1].append(sides[i])
		count += 1
list = new[0]+new[1]+new[2]
for line in list:
	sides = sorted(line, reverse=True)
	if sides[0] < sides[1]+sides[2]:
		triangles += 1
print triangles