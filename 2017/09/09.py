with open('09.in') as f:
    stream = f.readline().strip()
    counter = 0
    score = 0
    garbageCount = 0
    garbage = False
    skip = False

    for c in stream:
        if skip:
            skip = False
            continue
        if garbage and c != '!':
            if c == '>':
                garbage = False
            else:
                garbageCount += 1
            continue
        elif c == '!':
            skip = True
        elif c == '<':
            garbage = True
        elif c == '{':
            counter += 1
        elif c == '}':
            score += counter
            counter -= 1

    print score
    print garbageCount
