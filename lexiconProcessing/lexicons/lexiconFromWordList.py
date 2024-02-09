import sys
import epitran


epi = epitran.Epitran(sys.argv[1])
validCharacters = sys.argv[2]

line = sys.stdin.readline()

while line:
	
	formated = line.strip().lower()
	
	valid = True
	for character in formated:
		if character not in validCharacters:
			valid = False
			break
	
	if valid:
		sys.stdout.write(formated + "\t" + epi.transliterate(formated) + "\n")

	line = sys.stdin.readline()

		
	
	
