sum = 0
with open("04.txt", "r") as f:
	for line in f.readlines():
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
			sum += id
print sum