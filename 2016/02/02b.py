keypad = [["X", "X", "1", "X", "X"],["X", "2", "3", "4", "X"],["5", "6", "7", "8", "9"],["X", "A", "B", "C", "X"],["X", "X", "D", "X", "X"]]
current = [2, 0]
with open("02.txt", "r") as f:
	for line in f.readlines():
		count = 0
		for c in line:
			if c == "U":
				if current[0] > 0 and keypad[current[0]-1][current[1]] != "X":
					current[0] -= 1
			if c == "D":
				if current[0] < 4 and keypad[current[0]+1][current[1]] != "X":
					current[0] += 1
			if c == "R":
				if current[1] < 4 and keypad[current[0]][current[1]+1] != "X":
					current [1]+= 1
			if c == "L":
				if current[1] > 0 and keypad[current[0]][current[1]-1] != "X":
					current[1] -= 1
			count += 1
			if count == len(line):
				print keypad[current[0]][current[1]]