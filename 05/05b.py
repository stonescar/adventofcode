import hashlib
key = "ugkcyxxp"
n = 1
x = 0
code = ["x"]*8

while x < 8:
	hash = hashlib.md5(key+str(n)).hexdigest()
	if hash[0:5] == "00000" and hash[5] in "01234567" and code[int(hash[5])] == "x":
		code[int(hash[5])] = hash[6]
		x += 1
		print "".join(code)
	n += 1
print "Passord:", "".join(code)
