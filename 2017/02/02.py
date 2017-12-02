with open('02.txt') as f:
    checksum = 0
    for line in f.readlines():
        row = map(int, line.strip().split('\t'))
        checksum += max(row) - min(row)
    print checksum
