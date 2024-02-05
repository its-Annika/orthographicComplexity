import sys
import re
import random

pairs = sys.stdin.readlines()
storage = []
seenWords = []
exemplars = str(sys.argv[1])

currentLetter = pairs[1][0].lower()

for pair in pairs: 

	orthForm = pair.split("\t")[0].lower()
	ipaForm = re.sub("\s", "", pair.split("\t")[1])

	#throw out words over 25 characters	
	if len(orthForm) > 25:
		continue

	#prevent pronunciation of acronyms: <who> as "dʌbəljuːeɪt͡ʃəʊ"
	if len(orthForm) > len(ipaForm) * 2:
		continue

	#throw out words with invalid characters for the given langauge 
	invalid = False
	for character in orthForm:
		if character not in exemplars:
			invalid = True
			break

	if invalid:
		continue
			

	#keep only one pronucition of each word
	if orthForm in seenWords:
		continue

	else:
		seenWords.append(orthForm)
		curSet = [orthForm, ipaForm]
		storage += [curSet]

	#when the letter switches, clear the seenWords list to keep searching time down
	if orthForm[0] != currentLetter:
		currentLetter = orthForm[0]
		seenWords = []
		seenWords.append(orthForm)

random.shuffle(storage)

for i in range(7500):
	sys.stdout.write(storage[i][0] + "," + storage[i][1] + "\n")




