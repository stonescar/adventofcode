input = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
states = []

while True:
    blocks = max(input)
    currentIndex = input.index(blocks)
    input[currentIndex] = 0

    for i in range(blocks):
        currentIndex = (currentIndex+1) % len(input)
        input[currentIndex] += 1

    if input in states:
        break
    else:
        states.append(list(input))

print len(states)+1
print len(states)+1 - (states.index(input)+1)
