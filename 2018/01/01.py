with open("01.in") as f:
	freq = 0
	for s in f.readlines():
		freq += int(s.strip())
	print freq
