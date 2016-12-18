def tile(r):
	rows =[".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^."]
	count = rows[0].count(".")
	for i in range(r-1):
		new =""
		for t in range(100):
			if t == 0 and rows[i][t+1] == "^":
					new += "^" 
			elif t == 99 and rows[i][t-1] == "^":
				new += "^" 
			elif rows[i][t-1:t+2] == "^^." or rows[i][t-1:t+2] == "^.." or rows[i][t-1:t+2] == "..^" or rows[i][t-1:t+2] == ".^^":
				new += "^" 
			else:
				new += "."
				count += 1

		rows.append(new)
	return count

print tile(40)
print tile(400000)