with open('01.txt') as f:
    captcha = f.readline().strip()
    sum1 = 0
    sum2 = 0
    for i, x in enumerate(captcha):
        next = captcha[i+1] if i+1 != len(captcha) else captcha[0]
        opposite = captcha[(i+(len(captcha)/2)) % len(captcha)]
        if x == next:
            sum1 += int(x)
        if x == opposite:
            sum2 += int(x)
    print sum1
    print sum2
