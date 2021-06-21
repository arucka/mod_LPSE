results = {}

original = open("interpreted_LPSE-result-small_set.txt","r")
modif_1 = open("interpreted_modLPSE-result-small_set.txt","r")

for line in original:

	line_s = line.split("\t")
	passwd = line_s[0]
	score_original = line_s[3][:-1]
	
	lineM1 = modif_1.readline()
	line_s = lineM1.split("\t")
	if passwd != line_s[0]:
		print("Mismatch!")
	score_M1 = line_s[3][:-1]
	
	results[passwd] = (score_original,score_M1)

original.close()
modif_1.close()

print("Done loading.")

pcfg = open("interpreted_monte_carlo_results-small_set","r")
outfile = open("merged_results.txt","w")

outfile.write("Password\tPCFG\tLPSE\tModif_LPSE\n")

for line in pcfg :
	line_s = line.split("\t")
	passwd = line_s[0]
	score_pcfg = line_s[2][:-1]
	try:
		score_original, score_M1 = results[passwd]
		outfile.write(f"{passwd}\t{score_pcfg}\t{score_original}\t{score_M1}\n")
	except:
		print(f"Problems at password:\'{passwd}\'")

pcfg.close()
outfile.close()
