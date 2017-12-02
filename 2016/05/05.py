import hashlib
key = "ugkcyxxp"
n = 1
code = ""

while len(code) < 8:
	if hashlib.md5(key+str(n)).hexdigest()[0:5] == "00000":
		code += hashlib.md5(key+str(n)).hexdigest()[5]
	n += 1
print "Passord:", code