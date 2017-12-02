scr = [""]*8
message = ""
with open("06.txt", "r") as f:
	for line in f.readlines():
		l = line.rstrip()
		for c in range(8):
			if scr[c] == "":
				scr[c] = l[c]
			else:
				scr[c] += l[c]
for i in scr:
	chars = {}
	for c in i:
		if chars.has_key(c):
			chars[c] += 1
		else:
			chars[c] = 1
	chars2 = [(value, key) for key, value in chars.items()]
	message += min(chars2)[1]
print message