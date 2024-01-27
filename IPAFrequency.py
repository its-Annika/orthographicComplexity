import sys
from wordfreq import word_frequency
import re

pairs = sys.stdin.readlines()
languageCode = str(sys.argv[1])
freqStorage = []

for pair in pairs:
	orthForm = pair.split("\t")[0]
	ipaForm = re.sub("\s", "", pair.split("\t")[1])
			
	curSet = [orthForm, ipaForm, word_frequency(orthForm, languageCode)]
	freqStorage += [curSet] 

	
sortedFreq = sorted(freqStorage, key=lambda x: x[2], reverse=True)

randomizedHighFreq = sortedFreq[0:10000]

for i in range(5000):
	sys.stdout.write(randomizedHighFreq[i][0] + "\t" +  randomizedHighFreq[i][1] + "\n")
	



