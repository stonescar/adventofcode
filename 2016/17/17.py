import hashlib
from collections import deque

key = "njfxhljp"
q = deque()
q.append((0, 0, ""))

def check_doors(path):
	hash = hashlib.md5(key+path).hexdigest()[:4]
	open = ""
	for c in hash:
		open += "1" if c in "bcdef" else "0"
	return open

	
while len(q) > 0:
	x, y, p = q.pop()
	if (x, y) == (3, 3):
		print p
		break
	doors = check_doors(p)
	if doors[0] == "1" and y-1 >= 0:
		q.append((x, y-1, p+"U"))
	if doors[1] == "1" and y+1 < 4:
		q.append((x, y+1, p+"D"))
	if doors[2] == "1" and x-1 >= 0:
		q.append((x-1, y, p+"L"))
	if doors[3] == "1" and x+1 < 4:
		q.append((x+1, y, p+"R"))