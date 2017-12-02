with open("09.txt", "r") as f:
	inp = f.read()
	
def dec(x):
	mrk = False
	skip = 0
	decomp = ""

	a = ["", ""]
	b = 0
	for i in range(len(x)):
		if skip > 0:
			skip -= 1
		elif x[i] != "(" and not mrk:
			decomp += x[i]
		elif x[i] == "(" and not mrk:
			mrk = True
		elif mrk:
			if x[i] == "x":
				b = 1
			elif x[i] == ")":
				for j in range(int(a[1])):
					decomp += x[i+1:i+int(a[0])+1]
				mrk = False
				skip = int(a[0])
				a = ["", ""]
				b = 0
			else:
				a[b] += x[i]
				
	return decomp

print len(dec(inp))