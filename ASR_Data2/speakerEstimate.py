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

sentenceColumn = 2

with open(trainFilePath) as tf:

	firstLine = tf.readline()
	if firstLine.split("\t")[3] == "sentence":
		sentenceColumn = 3

	for line in tf:
		id = line.split("\t")[0]
		path = line.split("\t")[1]
		transcript = line.split("\t")[sentenceColumn]
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


while totalDuration < time:
	
	for speaker in speakerPool:
		for tripple in speakerDict[speaker]:
			audio = MP3(tripple[0])
			totalDuration += audio.info.length
		speakerCount += 1
		print(speakerCount, totalDuration)

print(task + " " + str(speakerCount))
		
