import sys
import os
import shutil
from pathlib import Path
from mutagen.mp3 import MP3
import random
import re

# FilePath, # audioFolderPath  #of speakers, #langCode, #task, #sentenceColumn


#read in and organize data
trainFilePath = sys.argv[1]
audioFolderPath = sys.argv[2]
speakerNumber = int(sys.argv[3]) -1
langCode = sys.argv[4]
task = sys.argv[5]

numFilesDict = {}
#{speakerID, number of files from them}
speakerDict = {}
#{speakerID, [(path,transcript),(),(),]

isHeader = True
sentenceColumn = 2

with open(trainFilePath) as tf:

	for line in tf:
		if isHeader:
			if line.split("\t")[3] == "sentence":
				sentenceColumn = 3
				isHeader = False

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
			numFilesDict[id] = 1



#pull the files as equally as possible from the chosen number of speakers
speakerPool = sorted(numFilesDict, key=numFilesDict.get, reverse=True)[:speakerNumber+1]


totalDuration = 0

dataSet = []

speaker = 0
count = 0

while totalDuration < 3600:
	if len(speakerDict[speakerPool[speaker]]) != 0:
		selected = random.choice(speakerDict[speakerPool[speaker]])
	#remove selected file to prevent duplicates
		temp = speakerDict[speakerPool[speaker]]
		temp.remove(selected)
		speakerDict[speakerPool[speaker]] = temp
		audio = MP3(selected[0])
		totalDuration += audio.info.length
		dataSet.append((selected[0], selected[1], audio.info.length, speakerPool[speaker]))

	if speaker == speakerNumber:
		speaker = 0
	else:
		speaker += 1


	count+=1

	if count % 500 == 0:
		print(totalDuration)

#print the dataFiles
totalDuration = 0
with open(langCode+"1Hour" + task + ".txt", "w+") as two:
	for path, transcript, duration, speaker in dataSet:
		two.write(path+","+transcript+","+str(duration)+","+speaker+"\n")
