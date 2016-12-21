string = "abcdefgh"

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
    if dir == "right":
        return s[len(s)-(x%len(s)):]+s[:len(s)-(x%len(s))]
    else:
        return s[x%len(s):]+s[:x%len(s)]

def rotP(s, l):
    for i in range(len(s)):
        if s[i] == l: x = i+1
    if x > 4:
        x += 1
    return rot(s, "right", x)

def rev(s, a, b):
    return s[:a]+"".join(reversed(s[a:b+1]))+s[b+1:]

def mv(s, a, b):
    if a < b:
        return s[:a]+s[a+1:b+1]+s[a]+s[b+1:]
    else:
        return s[:b]+s[a]+s[b:a]+s[a+1:]

with open("21.in") as f:
    for line in f:
        l = line.strip().split(" ")
        if l[0] == "swap":
            string = swap(string, l[2], l[5])
        elif l[0] == "rotate" and l[1] != "based":
            string = rot(string, l[1], int(l[2]))
        elif l[0] == "rotate" and l[1] == "based":
            string = rotP(string, l[6])
        elif l[0] == "reverse":
            string = rev(string, int(l[2]), int(l[4]))
        else:
            string = mv(string, int(l[2]), int(l[5]))
            
print string

print rotP("abcdefgh", "g")