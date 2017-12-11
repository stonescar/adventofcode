with open('11.in') as f:
    directions = f.readline().split(',')
    max_dist = 0

    def calc_dist(dirs):
        steps = {
            'n':    dirs.count('n,'),
            's':    dirs.count('s,'),
            'nw':   dirs.count('nw'),
            'ne':   dirs.count('ne'),
            'sw':   dirs.count('sw'),
            'se':   dirs.count('se')
        }

        ns = min(steps['n'], steps['s'])
        nwse = min(steps['nw'], steps['se'])
        nesw = min(steps['ne'], steps['sw'])

        steps['n'] -= ns
        steps['s'] -= ns
        steps['nw'] -= nwse
        steps['se'] -= nwse
        steps['ne'] -= nesw
        steps['sw'] -= nesw

        nws = min(steps['nw'], steps['s'])
        steps['nw'] -= nws
        steps['s'] -= nws
        steps['sw'] += nws

        nes = min(steps['ne'], steps['s'])
        steps['ne'] -= nes
        steps['s'] -= nes
        steps['se'] += nes

        swn = min(steps['sw'], steps['n'])
        steps['sw'] -= swn
        steps['n'] -= swn
        steps['nw'] += swn

        sen = min(steps['se'], steps['n'])
        steps['se'] -= sen
        steps['n'] -= sen
        steps['ne'] += sen

        sesw = min(steps['se'], steps['sw'])
        steps['se'] -= sesw
        steps['sw'] -= sesw
        steps['s'] += sesw

        nenw = min(steps['ne'], steps['nw'])
        steps['ne'] -= nenw
        steps['nw'] -= nenw
        steps['n'] += nenw

        return sum(s for s in steps.values())

    print calc_dist(','.join(directions))

    for i in range(len(directions)):
        max_dist = max(max_dist, calc_dist(','.join(directions[:i])))

    print max_dist
