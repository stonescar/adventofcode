input = "00111101111101000"

def dragon(a):
    b = ""
    for i in reversed(a):
        if i == "1":
            b += "0"
        else:
            b += "1"
    return a+"0"+b
            
    
def check(a):
    sum = ""
    for i in range(0,len(a),2):
        if a[i] == a[i+1]:
            sum += "1"
        else:
            sum += "0"
    return sum

while len(input) < 35651584:
    input = dragon(input)
    
input = check(input[:35651584])

while len(input) % 2 == 0:
    input = check(input)

print input