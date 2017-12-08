with open('08.in') as f:
    regs = {}
    highest = 0
    for line in f.readlines():
        inst = line.strip().split(' ')
        name = inst[0]
        inc = 0+int(inst[2]) if inst[1] == 'inc' else 0-int(inst[2])

        if name not in regs.keys():
            regs[name] = 0

        if inst[4] not in regs.keys():
            regs[inst[4]] = 0

        if inst[5] == '==' and regs[inst[4]] == int(inst[6]):
            regs[name] += inc
        if inst[5] == '<' and regs[inst[4]] < int(inst[6]):
            regs[name] += inc
        if inst[5] == '>' and regs[inst[4]] > int(inst[6]):
            regs[name] += inc
        if inst[5] == '<=' and regs[inst[4]] <= int(inst[6]):
            regs[name] += inc
        if inst[5] == '>=' and regs[inst[4]] >= int(inst[6]):
            regs[name] += inc
        if inst[5] == '!=' and regs[inst[4]] != int(inst[6]):
            regs[name] += inc

        highest = max(highest, max(regs.values()))

    print max(regs.values())
    print highest
