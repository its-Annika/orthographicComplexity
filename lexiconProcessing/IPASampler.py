import sys
import re
import random 

pairs = sys.stdin.readlines()
storage = []
seenWords = []


currentLetter = pairs[1][0].lower()

for pair in pairs: 

	orthForm = pair.split("\t")[0].lower()
	ipaForm = re.sub("\s", "", pair.split("\t")[1])
	

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




