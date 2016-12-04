def uncr(inp, id):
	a = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
	b = "abcdefghijklmnopqrstuvwxyz"
	words = inp.split("-")
	unc = ""
	for w in words:
		for c in w:
			start = a[c]-1
			unc += b[(start+id)%26]
		unc += " "
	return unc, id

rooms = []
with open("04.txt", "r") as f:
	for line in f.readlines():
		name = line.rstrip()
		name = name[:len(name)-11]
		a = line.rstrip().split("-")
		id = a[len(a)-1]
		a.remove(a[len(a)-1])
		letters = ""
		for i in range(len(a)):
			letters += a[i]
		check = id[4:len(id)-1]
		id = int(id[:3])
		
		count = {}
		for char in letters:
			if count.has_key(char):
				count[char] += 1
			else:
				count[char] = 1
		count2 = {}
		for i in count:
			if count2.has_key(count[i]):
				count2[count[i]] += i
			else:
				count2[count[i]] = i
		for i in count2:
			count2[i] = "".join(sorted(count2[i]))
		sort = ""
		sort2 = []
		for i in count2:
			sort2.append(i)
		for i in reversed(sort2):
			sort += count2[i]
		
		
		if check == sort[:5]:
			rooms.append(uncr(name, id))

for r in rooms:
	if "north" in r[0]:
		print r