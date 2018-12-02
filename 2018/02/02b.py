with open("02.in") as f:
	boxes = []
	for i, l in enumerate(f.readlines()):
		if i == 0:
			boxes.append(l.strip())
		else:
			for b in boxes:
				x = []
				u = zip(b, l.strip())
				for j,k in u:
					x.append(j if j == k else "*" )
				if x.count("*") == 1:
					print "".join(x).replace("*", "")
					break
			boxes.append(l.strip())
