sum = 0
with open("07.txt", "r") as f:
	for line in f.readlines():
		aba = []
		bab = []
		br = False
		ssl = False
		for i in range(len(line)-2):
			if line[i] == "[":
				br = True
			elif line[i] == "]":
				br = False
			else:
				if line[i] == line[i+2] and line[i+1] and line[i] != line[i+1] not in "[]" and not br:
					aba.append(line[i:i+3])
				if line[i] == line[i+2] and line[i+1] and line[i] != line[i+1] not in "[]" and br:
					bab.append(line[i:i+3])
		for a in aba:
			for b in bab:
				if a == b[1:3]+b[1]:
					ssl = True
		if ssl:
			sum += 1
print sum