import sys
import os
import shutil
from pathlib import Path
from mutagen.mp3 import MP3
import random
import re

# trainFilePath, # audioFolderPath  #langCode, time, task


#read in and organize data
trainFilePath = sys.argv[1]
audioFolderPath = sys.argv[2]
langCode = sys.argv[3]
time = int(sys.argv[4])
task = sys.argv[5]

numFilesDict = {}
#{speakerID, # of files they have}
speakerDict = {}
#{speakerID, [(path,transcript),(),(),]


with open(trainFilePath) as tf:

	next(tf)

	for line in tf:

		id = line.split("\t")[0]
		path = line.split("\t")[1]
		transcript = line.split("\t")[3]
		cleanTranscript = re.sub("[.,!?\"\'`#@$^&*\(\)\[\]]", "", transcript).lower()

		attributes = (audioFolderPath+path,cleanTranscript)

		if id in speakerDict.keys():
			speakerDict[id].append(attributes)
			numFilesDict[id] += 1
		else:
			speakerDict[id] = [attributes]
			numFilesDict[id] = 0



#pull the files as equally as possible from the chosen number of speakers
speakerPool = sorted(numFilesDict, key=numFilesDict.get, reverse=True)


totalDuration = 0
speakerCount = 0

for speaker in speakerPool:
	speakerCount += 1
	for tripple in speakerDict[speaker]:
		audio = MP3(tripple[0])
		totalDuration += audio.info.length

	if totalDuration > time:
		break

print(task + " " + str(speakerCount))
