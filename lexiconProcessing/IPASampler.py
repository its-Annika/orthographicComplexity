import sys
import re
import random
import unicodedata

pairs = sys.stdin.readlines()
storage = []
invalidExemplars = str(sys.argv[1])

for pair in pairs: 

	orthForm = pair.split("\t")[0].lower()
	ipaForm = re.sub("\s", "", pair.split("\t")[1]) 

	#throw out words over 25 characters	
	if len(orthForm) > 25 or len(ipaForm) > 25:
		continue

	#prevent pronunciation of acronyms: <who> as "dʌbəljuːeɪt͡ʃəʊ"
	if len(orthForm) > len(ipaForm) * 2:
		continue

	#throw out words with invalid characters for the given langauge 
	invalid = False
	for character in orthForm:
		if character in invalidExemplars or "L" not in unicodedata.category(character):
			invalid = True
			break

	if not invalid:
		curSet = [orthForm, ipaForm]
		storage.append(curSet)

random.shuffle(storage)

for i in range(7500):
	sys.stdout.write(storage[i][0] + "," + storage[i][1] + "\n")




