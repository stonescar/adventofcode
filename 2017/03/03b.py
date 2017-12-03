def sumAdjacent():
    x, y = current[0], current[1]
    return sum([grid[x-1][y-1],
                grid[x-1][y],
                grid[x-1][y+1],
                grid[x][y-1],
                grid[x][y+1],
                grid[x+1][y-1],
                grid[x+1][y],
                grid[x+1][y+1]])


def turnIfOpen():
    left = dirs[(dir+1) % 4]
    if grid[current[0]+left[0]][current[1]+left[1]] == 0:
        return (dir+1) % 4
    else:
        return dir


input = 361527
gridSize = 11
grid = [[0 for i in range(gridSize)] for j in range(gridSize)]

current = [gridSize/2, gridSize/2]
grid[current[0]][current[1]] = 1
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # E N W S
dir = 3

while True:
    dir = turnIfOpen()
    current[0] += dirs[dir][0]
    current[1] += dirs[dir][1]
    num = sumAdjacent()
    grid[current[0]][current[1]] = num
    if num > input:
        print num
        break
