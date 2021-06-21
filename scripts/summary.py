infile = open("merged_results.txt","r")
headline = infile.readline()

dist = {"weak": 0, "medium": 0, "strong": 0}

ctrs = {"strong": {"lpse": {"strong": 0, "medium": 0, "weak": 0}, "mod_1": {"strong": 0, "medium": 0, "weak": 0}}, "medium": {"lpse": {"strong": 0, "medium": 0, "weak": 0}, "mod_1": {"strong": 0, "medium": 0, "weak": 0}}, "weak": {"lpse": {"strong": 0, "medium": 0, "weak": 0}, "mod_1": {"strong": 0, "medium": 0, "weak": 0}}}

for line in infile:
	line = line[:-1]
	scores = line.split("\t")[1:]
	pcfg = scores[0]
	dist[pcfg] += 1
	for algo, score in zip(["lpse","mod_1"],scores[1:]):
		ctrs[pcfg][algo][score] += 1

infile.close()

print(f"Passwords distribution:\nWeak: {dist['weak']}\tMedium: {dist['medium']}\tStrong: {dist['strong']}\n")
print(f"STRONG PASSWORDS CLASSIFICATION")
print("Algo\tStrong\tMedium\tWeak")
print(f"LPSE\t{ctrs['strong']['lpse']['strong']}\t{ctrs['strong']['lpse']['medium']}\t{ctrs['strong']['lpse']['weak']}")
print(f"Mod_1\t{ctrs['strong']['mod_1']['strong']}\t{ctrs['strong']['mod_1']['medium']}\t{ctrs['strong']['mod_1']['weak']}")
print(f"WEAK PASSWORDS CLASSIFICATION")
print("Algo\tStrong\tMedium\tWeak")
print(f"LPSE\t{ctrs['weak']['lpse']['strong']}\t{ctrs['weak']['lpse']['medium']}\t{ctrs['weak']['lpse']['weak']}")
print(f"Mod_1\t{ctrs['weak']['mod_1']['strong']}\t{ctrs['weak']['mod_1']['medium']}\t{ctrs['weak']['mod_1']['weak']}")
