with open('05.in') as f:
    def strip_lines(input):
        return int(input.strip())
    offsets = map(strip_lines, f.readlines())

    currentIndex = 0
    nextIndex = 0
    count = 0

    while nextIndex >= 0 and nextIndex < len(offsets):
        currentIndex = nextIndex
        nextIndex = currentIndex + offsets[currentIndex]
        # offsets[currentIndex] += 1     <=== Part 1
        offsets[currentIndex] += 1 if offsets[currentIndex] < 3 else -1  # <?=== Part 2
        count += 1

    print count
