import sys

occurences = {}

def include_trigram(trigram):
	if occurences.get(trigram) == None:
		occurences[trigram] = 1
	else:
		occurences[trigram] += 1

def calculate_occurences(infile):
	for line in infile:
			LEN = len(line)
			i = 0
			while i < LEN-2 :
				if line[i].isalpha():
					if line[i+1].isalpha():
						if line[i+2].isalpha():
							include_trigram(line[i:i+3].lower())
							i += 1
						else:
							i += 3
					else:
						i += 2
				else:
					i += 1

def sort_desc_by_occurence():
	trigrams = list(occurences.items())
	trigrams.sort(reverse=True, key=lambda tri_occ: tri_occ[1])
	return trigrams

def main():
	
	fname = sys.argv[1]
	if len(sys.argv) > 2:
		n = int(sys.argv[2])
	else:
		n = 20

	infile = open(fname,"r")
	calculate_occurences(infile)
	infile.close()
	
	trigrams_desc = sort_desc_by_occurence()
	
	outfile = open(f"trigrams_{fname}","w")
	OUTFILE = open(f"TRIGRAMS_{fname}","w")
	if n > len(trigrams_desc):
		n = len(trigrams_desc)
	for trigram,_ in trigrams_desc[:n]:
		outfile.write(f"{trigram}\n")
		OUTFILE.write(f"{trigram.upper()}\n")
	outfile.close()
	OUTFILE.close()

if __name__ == "__main__":
	main()
