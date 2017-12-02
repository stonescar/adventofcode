coor = [0, 0]
dir = 0 #0=N 1=E 2=S 3=W
visited = []

with open("01.txt", "r") as f:
    commands = f.readline().split(", ")

for c in commands:
    if c[0] == "L":
        dir -= 1
        if dir < 0:
            dir = 3
    elif c[0] == "R":
        dir += 1
        if dir > 3:
            dir = 0
    for i in range(int(c[1:])):
        if dir == 0:
            coor[1] += 1
        elif dir == 1: 
            coor[0] += 1
        elif dir == 2: 
            coor[1] -= 1
        elif dir == 3: 
            coor[0] -= 1
            
        if str(coor[0])+", "+str(coor[1]) in visited:
            print coor
            print abs(coor[0])+abs(coor[1])
            break
        else:
            visited.append(str(coor[0])+", "+str(coor[1]))
    else:
        continue
    break