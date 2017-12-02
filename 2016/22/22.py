nodes = []
pairs = []
with open("22.in") as f:
	for line in f:
		if "node-" in line:
			l = line.strip().split()
			nodes.append([int(l[2][:len(l[2])-1]), int(l[3][:len(l[3])-1]), l[0].split("e-")[1]])

for i in range(len(nodes)):
	for j in range(len(nodes)):
		if i != j and nodes[i][0] <= nodes[j][1] and "".join(sorted([nodes[i][2], nodes[j][2]])) not in pairs and nodes[i][0] != 0:
			pairs.append(" - ".join(sorted([nodes[i][2], nodes[j][2]])))

print len(pairs)