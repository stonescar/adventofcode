current = 5

with open("02.txt", "r") as f:
	for line in f.readlines():
		count = 0
		for c in line:
			if c == "U":
				if current > 3:
					current -= 3
			if c == "D":
				if current < 7:
					current += 3
			if c == "R":
				if current %3 != 0:
					current += 1
			if c == "L":
				if current %3 != 1:
					current -= 1
			count += 1
			if count == len(line):
				print current