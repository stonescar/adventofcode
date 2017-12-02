grid = []
for i in range(50):
	grid.append([])
	
def pr_gr():
	for i in grid:
		print "".join(i)

def find_wall(x, y):
	if str(bin((x*x+3*x+2*x*y+y+y*y)+1350)[2:]).count("1") %2 == 0:
		return " "
	else:
		return u"\u2588"
		
for i in range(len(grid)):
	for j in range(len(grid)):
		grid[i].append(find_wall(i, j))


from collections import deque, defaultdict

q = deque()
q.append((1, 1))
count = defaultdict(dict)
count[1][1] = 0
grid[1][1] = "+"

while len(q) > 0:
	x, y = q.popleft()
	if (x, y) == (31, 39):
		grid[x][y] = "O"
		break
	if x+1 < len(grid) and grid[x+1][y] == " ":
		q.append((x+1, y))
		count[x+1][y] = count[x][y] + 1
	if y+1 < len(grid) and grid[x][y+1] == " ":
		q.append((x, y+1))
		count[x][y+1] = count[x][y] + 1
	if x-1 >= 0 and grid[x-1][y] == " ":
		q.append((x-1, y))
		count[x-1][y] = count[x][y] + 1
	if y-1 >= 0 and grid[x][y-1] == " ":
		q.append((x, y-1))
		count[x][y-1] = count[x][y] + 1
	grid[x][y] = "+"

pr_gr()
print count[31][39]