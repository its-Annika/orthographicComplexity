# arg 1 = train/test file
# arg 2 = comparison file

import sys


paths = []
with open(sys.argv[1]) as f:
	for line in f:
		line1 = line.strip("\n")
		bits = line1.split('/')
		paths.append(bits[-1])



pathDict = {}
with open(sys.argv[2]) as f2:
	for line in f2:
		path = line.split()[1]
		speaker = line.split()[0]
		pathDict[path] = speaker


speakerDict = {}

for path in paths:
	speaker = pathDict[path]
	speakerDict[speaker] = path


print(len(speakerDict.keys()))
