string = "fbgdceah"

def swap(s, a, b):
    i = []
    if a.isdigit():
        i = [int(a), int(b)]
    else:
        for l in range(len(s)):
            if s[l] == a or s[l] == b:
                i.append(l)
    return s[0:min(i)]+s[max(i)]+s[min(i)+1:max(i)]+s[min(i)]+s[max(i)+1:]

def rot(s, dir, x):
    if dir == "left":
        return s[len(s)-(x%len(s)):]+s[:len(s)-(x%len(s))]
    else:
        return s[x%len(s):]+s[:x%len(s)]

def rotP(s, l):
    x = s.find(l)+1
    if x > 4:
        x += 1
    return rot(s, "left", x)

def rotP2(s, l):
    x = 0
    for i in range(len(s)):
        if rotP(rot(s, "left", i), l) == s:
            return rot(s, "left", i)
            break

def rev(s, a, b):
    return s[:a]+"".join(reversed(s[a:b+1]))+s[b+1:]

def mv(s, b, a):
    if a < b:
        return s[:a]+s[a+1:b+1]+s[a]+s[b+1:]
    else:
        return s[:b]+s[a]+s[b:a]+s[a+1:]


with open("21.in") as f:
    for line in reversed(f.readlines()):
        l = line.strip().split(" ")
        if l[0] == "swap":
            string = swap(string, l[2], l[5])
        elif l[0] == "rotate" and l[1] != "based":
            string = rot(string, l[1], int(l[2]))
        elif l[0] == "rotate" and l[1] == "based":
            string = rotP2(string, l[6])
        elif l[0] == "reverse":
            string = rev(string, int(l[2]), int(l[4]))
        else:
            string = mv(string, int(l[2]), int(l[5]))
            
print string