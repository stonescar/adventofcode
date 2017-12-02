with open('02.txt') as f:
    checksum = 0
    for line in f.readlines():
        row = map(int, line.strip().split('\t'))
        for i, x in enumerate(row):
            for y in row[i+1:]:
                if max(x, y) % min(x, y) == 0:
                    checksum += max(x, y) / min(x, y)
    print checksum
