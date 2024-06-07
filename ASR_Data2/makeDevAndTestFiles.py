import sys
import os
import shutil
from pathlib import Path
from mutagen.mp3 import MP3
import random
import re

# trainFilePath, # audioFolderPath  #of speakers, #langCode, #task


#read in and organize data
trainFilePath = sys.argv[1]
audioFolderPath = sys.argv[2]
speakerNumber = int(sys.argv[3])
langCode = sys.argv[4]
task = sys.argv[5]

numFilesDict = {}
#{speakerID, number of files from them}
speakerDict = {}
#{speakerID, [(path,transcript),(),(),]

with open(trainFilePath) as tf:
	next(tf)
	for line in tf:
		id = line.split("\t")[0]
		path = line.split("\t")[1]
		transcript = line.split("\t")[2]
		cleanTranscript = re.sub("[.,!?\"\'`#@$^&*\(\)\[\]]", "", transcript).lower()

		attributes = (audioFolderPath+path,cleanTranscript)

		if id in speakerDict.keys():
			speakerDict[id].append(attributes)
			numFilesDict[id] += 1
		else:
			speakerDict[id] = [attributes]
			numFilesDict[id] = 1



#pull the files as equally as possible from the chosen number of speakers
speakerPool = sorted(numFilesDict, key=numFilesDict.get, reverse=True)[:speakerNumber+1]


totalDuration = 0

dataSet = []

speaker = 0

while totalDuration < 9000:
	if len(speakerDict[speakerPool[speaker]]) != 0:
		selected = random.choice(speakerDict[speakerPool[speaker]])
	#remove selected file to prevent duplicates
		temp = speakerDict[speakerPool[speaker]]
		temp.remove(selected)
		speakerDict[speakerPool[speaker]] = temp
		dataSet.append(selected)
		audio = MP3(selected[0])
		totalDuration += audio.info.length

	if speaker == speakerNumber:
		speaker = 0
	else:
		speaker += 1

#print the dataFiles
totalDuration = 0
with open(langCode+"2.5Hour" + task + ".txt", "w+") as two:
	for path, transcript in dataSet:
		two.write(path+","+transcript+"\n")
