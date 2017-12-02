bots = []
outputs = {}
class bot:	
	full = 0
	def __init__(self, name, lt, l, ht, h):
		self.name = name
		self.low = [lt, l]
		self.high = [ht, h]
		self.chips = []
	
	def pr_bot(self):
		if len(self.chips) == 2:
			print "Bot %s gives low to %s %s and high to %s %s and have %s chips (%s and %s)" % (self.name, self.low[0], self.low[1], self.high[0], self.high[1], len(self.chips), self.chips[0], self.chips[1])
		elif len(self.chips) == 1:
			print "Bot %s gives low to %s %s and high to %s %s and have %s chip (%s)" % (self.name, self.low[0], self.low[1], self.high[0], self.high[1], len(self.chips), self.chips[0])
		else:
			print "Bot %s gives low to %s %s and high to %s %s and have no chips" % (self.name, self.low[0], self.low[1], self.high[0], self.high[1])

def set(bt, val):
	for b in bots:
		if b.name == bt:
			b.chips.append(val)

def check2():
	bot.full = 0
	for b in bots:
		if len(b.chips) == 2:
			bot.full += 1

def distr():
	while bot.full > 0:
		for b in bots:
			if len(b.chips) == 2:
				if 61 in b.chips and 17 in b.chips:
					print "---> ",
					b.pr_bot()
				if b.low[0] == "bot":
					for c in bots:
						if c.name == b.low[1]:
							c.chips.append(min(b.chips))
				else:
					outputs[b.low[1]] = min(b.chips)
				if b.high[0] == "bot":
					for c in bots:
						if c.name == b.high[1]:
							c.chips.append(max(b.chips))
				else:
					outputs[b.high[1]] = max(b.chips)
				b.chips = []
		check2()
			
			
with open("10.txt", "r") as f:
	for line in f.readlines():
		line = line.strip().split(" ")
		if line[0] == "bot":
			bots.append(bot(int(line[1]), line[5], int(line[6]), line[10], int(line[11])))
			
	
with open("10.txt", "r") as f:
	for line in f.readlines():
		line = line.strip().split(" ")
		if line[0] == "value":
			set(int(line[5]), int(line[1]))
			check2()
			distr()

print outputs[0]*outputs[1]*outputs[2]