with open('04.in') as f:
    valid = 0
    for line in f.readlines():
        phrase = line.strip().split(' ')
        v = True
        for word in phrase:
            if phrase.count(word) > 1:
                v = False
                continue
        if v:
            valid += 1
    print valid
