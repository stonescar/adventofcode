disp = [["."] *50, ["."] *50, ["."] *50, ["."] *50, ["."] *50, ["."] *50]
def pr_disp():
	for l in disp:
		print "".join(l)

def count():
	sum = 0
	for r in disp:
		for c in r:
			if c == "#":
				sum += 1
	return sum
		
def rect(a, b):
	for x in range(a):
		for y in range(b):
			disp[y][x] = "#"

def rot_r(a, s):
	old = disp[a]
	disp[a] = ["."]*len(old)
	for i in range(len(old)):
		if old[i] == "#":
			disp[a][(i+s)%len(old)] = "#"

def rot_c(a, s):
	old = []
	for i in range(len(disp)):
		old.append(disp[i][a])
		disp[i][a] = "."
	for i in range(len(old)):
		if old[i] == "#":
			disp[(i+s)%len(disp)][a] = "#"
	

with open("08.txt", "r") as f:
	for line in f.readlines():
		l = line.strip().split(" ")
		if l[0] == "rect":
			xy = l[1].split("x")
			rect(int(xy[0]), int(xy[1]))
		if l[0] == "rotate" and l[1] == "row":
			rot_r(int(l[2][2:]), int(l[4]))
		if l[0] == "rotate" and l[1] == "column":
			rot_c(int(l[2][2:]), int(l[4]))
			
pr_disp()
print count()