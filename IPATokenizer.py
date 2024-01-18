#takes a file with one word per line
#Python3 convertToIPA.py, language code, valid symbols

import sys
import epitran
from collections import defaultdict

words = sys.stdin.readlines()
languageCode = str(sys.argv[1])
validSymbols = str(sys.argv[2])
epi = epitran.Epitran(languageCode)
seenWords = defaultdict(lambda:0)


for word in words:
	
	cleanWord = word.strip("\n").lower()

	valid = True
	for character in cleanWord:
		if character not in validSymbols:
			valid = False
			break
	
	if valid:

		if cleanWord in seenWords.keys():
			pass
		
		else:
			seenWords[cleanWord] += 1
			sys.stdout.write(cleanWord.strip("\n") + "\t" + epi.transliterate(cleanWord.strip("\n")) + "\n")
