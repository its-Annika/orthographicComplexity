import sys
from wordfreq import word_frequency
import re

pairs = sys.stdin.readlines()
languageCode = str(sys.argv[1])
freqStorage = []
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
		curSet = [orthForm, ipaForm, word_frequency(orthForm, languageCode)]
		freqStorage += [curSet]

	#when the letter switches, clear the seenWords list to keep searching time down
	if orthForm[0] != currentLetter:
		currentLetter = orthForm[0]
		seenWords = []
		seenWords.append(orthForm)

	
sortedFreq = sorted(freqStorage, key=lambda x: x[2], reverse=True)

highFreq = sortedFreq[0:7500]

for word, pronouncation, freq in highFreq:
	sys.stdout.write(word +  "," + pronouncation + "\n")
	



