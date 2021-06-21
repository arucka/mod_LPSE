import sys

WEAK_TRESHOLD = 10**10
STRONG_TRESHOLD = 10**14

def analyze(passwd):
	lower = []
	upper = []
	digits = []
	special = []
	for char in passwd:
		if char.isalpha():
			if char.islower():
				if char not in lower:
					lower.append(char)
			else:
				if char not in upper:
					upper.append(char)
		elif char.isdigit():
			if char not in digits:
				digits.append(char)
		else:
			if char not in special:
				special.append(char)
	return (lower,upper,digits,special)

def has2Types(analysis):
	ctr = 0
	for elem in analysis:
		if len(elem) > 0:
			ctr += 1
	return (ctr >= 2)

def has5DiffChars(analysis):
	ctr = 0
	for elem in analysis:
		ctr += len(elem)
	return (ctr >= 5)
	

def strength(rank,passwd):
	if rank <= WEAK_TRESHOLD:
		return "weak"
	# otherwise check three conditions for a strong password
	# CONDITION 1
	if rank >= STRONG_TRESHOLD:
		analysis = analyze(passwd)
		# CONDITION 2
		if has2Types(analysis) or len(passwd) >= 12 :
			# CONDITION 3
			if has5DiffChars(analysis) :
				return "strong"
	# otherwise it's medium
	return "medium"

def main():
	fname = sys.argv[1]
	infile = open(fname,"r")
	outfile = open(f"interpreted_{fname}","w")
	for line in infile:
		line_s = line.split("\t")
		passwd = line_s[0]
		rank = int(line_s[3])
		score = strength(rank,passwd)
		outfile.write(f"{passwd}\t{rank}\t{score}\n")
	infile.close()
	outfile.close()

if __name__ == "__main__":
	main()
