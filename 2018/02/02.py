import re

def two(string):
	sorted_str = "".join(sorted(string))
	doubles = re.compile(r"(\w)\1").findall(sorted_str)
	if len(doubles) == 0:
		return False
	for c in doubles:
		if string.count(c) == 2:
			return True
	return False

def three(string):
	rx = re.compile(r"(\w)\1{2}")
	sorted_str = "".join(sorted(string))
	return not not rx.search(sorted_str)

with open("02.in") as f:
	twos = 0
	threes = 0

	for l in f.readlines():
		twos += 1 if two(l.strip()) else 0
		threes += 1 if three(l.strip()) else 0

	print twos, threes
	print twos * threes
