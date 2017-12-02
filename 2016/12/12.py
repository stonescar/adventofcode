reg = {"a": 0, "b": 0, "c": 1, "d": 0}
comm = []

with open("12.txt", "r") as f:
	for line in f.readlines():
		comm.append(line.strip().split(" "))

c = 0

while c < len(comm):
	if comm[c][0] == "cpy":
		if comm[c][1].isdigit():
			reg[comm[c][2]] = int(comm[c][1])
		else: reg[comm[c][2]] = reg[comm[c][1]]
	elif comm[c][0] == "inc":
		reg[comm[c][1]] += 1
	elif comm[c][0] == "dec":
		reg[comm[c][1]] -= 1
	elif comm[c][0] == "jnz":
		if (comm[c][1].isdigit() and comm[c][1] != 0) or (not comm[c][1].isdigit() and reg[comm[c][1]] != 0):
			c += int(comm[c][2])-1
	c += 1

for r in reg:
	print r, reg[r]
