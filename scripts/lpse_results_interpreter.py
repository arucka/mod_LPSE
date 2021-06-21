import sys

def strength(cls,pds):
	if cls >= 0.4 or pds >= 0.55 :
		return "strong"
	if ( 0.3 <= cls < 0.4 ) and ( 0.4 <= pds < 0.55 ) :
		return "strong"
	if cls <= 0.19 or pds < 0.35 :
		return "weak"
	return "medium"

def main():
	fname = sys.argv[1]
	infile = open(fname,"r")
	outfile = open(f"interpreted_{fname}","w")
	for line in infile:
		line_s = line.split("\t")
		passwd = line_s[0]
		cls = float(line_s[1])
		pds = float(line_s[2])
		score = strength(cls,pds)
		outfile.write(f"{passwd}\t{cls}\t{pds}\t{score}\n")
	infile.close()
	outfile.close()

if __name__ == "__main__":
	main()
