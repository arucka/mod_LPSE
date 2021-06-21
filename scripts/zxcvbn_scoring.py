# Scores the passwords according to zxcvbn algorithm and translated the score to LPSE scale
# Ouput format:
# password zxcvbn_score LPSE_score

from zxcvbn import zxcvbn
import sys

def translate_to_LPSE(zxcvbn_score):
	if zxcvbn_score <= 1:
		return "weak"
	elif zxcvbn_score == 2:
		return "medium"
	else:
		return "strong"

def main():
	infile = open(sys.argv[1],"r")
	outfile = open("zxcvbn_score-small_set.txt","w")
	
	errors = 0

	for line in infile:
		passwd = line[:-1]
		try:
			result = zxcvbn(passwd)
			zxcvbn_score = result['score']
			lpse_score = translate_to_LPSE(zxcvbn_score)
			outfile.write(f"{passwd}\t{zxcvbn_score}\t{lpse_score}\n")
		except:
			errors += 1

	infile.close()
	outfile.close()
	
	print(f"Done. {errors} errors.")

if __name__ == "__main__":
	main()
