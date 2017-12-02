sum = 0
with open("07.txt", "r") as f:
	for line in f.readlines():
		a = ","
		br = False
		tls = 0
		for i in range(len(line)):
			if line[i] == "[":
				br = True
			elif line[i] == "]":
				br = False
			else:
				if br and line[i] != a and line[i]+a == line[i+1:i+3]:
					tls -= 99999
					break
				elif line[i] != a and line[i]+a == line[i+1:i+3]:
					tls += 1
				a = line[i]
		if tls > 0:
			sum +=1
print sum