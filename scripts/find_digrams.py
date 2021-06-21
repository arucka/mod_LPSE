import sys

occurences = {}

def include_digram(digram):
	if occurences.get(digram) == None:
		occurences[digram] = 1
	else:
		occurences[digram] += 1

def calculate_occurences(infile):
	for line in infile:
			LEN = len(line)
			i = 0
			while i < LEN-1 :
				if line[i].isalpha():
					if line[i+1].isalpha():
						include_digram(line[i:i+2].lower())
						i += 1
					else:
						i += 2
				else:
					i += 1

def sort_desc_by_occurence():
	digrams = list(occurences.items())
	digrams.sort(reverse=True, key=lambda di_occ: di_occ[1])
	return digrams

def main():
	
	fname = sys.argv[1]
	if len(sys.argv) > 2:
		n = int(sys.argv[2])
	else:
		n = 30

	infile = open(fname,"r")
	calculate_occurences(infile)
	infile.close()
	
	digrams_desc = sort_desc_by_occurence()
	
	outfile = open(f"digrams_{fname}","w")
	OUTFILE = open(f"DIGRAMS_{fname}","w")
	if n > len(digrams_desc):
		n = len(digrams_desc)
	for digram,_ in digrams_desc[:n]:
		outfile.write(f"{digram}\n")
		OUTFILE.write(f"{digram.upper()}\n")
	outfile.close()
	OUTFILE.close()

if __name__ == "__main__":
	main()
