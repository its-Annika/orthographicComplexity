import sys
import os
import shutil
from pathlib import Path
from mutagen.mp3 import MP3
import random
import re

# trainFilePath, # audioFolderPath  #of speakers, #langCode


#read in and organize data
trainFilePath = sys.argv[1]
audioFolderPath = sys.argv[2]
speakerNumber = int(sys.argv[3]) 
langCode = sys.argv[4]

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
speakerPool = sorted(numFilesDict, key=numFilesDict.get, reverse=True)[:speakerNumber]

totalDuration = 0

dataSet = []

speaker = 0
count = 0

while totalDuration < 36000:
	if len(speakerDict[speakerPool[speaker]]) != 0:
		selected = random.choice(speakerDict[speakerPool[speaker]])
	#remove selected file to prevent duplicates
		temp = speakerDict[speakerPool[speaker]]
		temp.remove(selected)
		speakerDict[speakerPool[speaker]] = temp
		audio = MP3(selected[0])
		totalDuration += audio.info.length
		dataSet.append((selected[0], selected[1], audio.info.length, speakerPool[speaker]))

	if speaker + 1  == speakerNumber:
		speaker = 0
	else:
		speaker += 1

	count+=1

	if count % 500 == 0:
		print(totalDuration)

#print the dataFiles
totalDuration = 0
with open(langCode+"2.5HourTrain.txt", "w+") as two, open(langCode+"5HourTrain.txt", "w+") as five, open(langCode+"10HourTrain.txt", "w+") as ten:
	for path, transcript, duration, speaker in dataSet:
		totalDuration += duration
		if totalDuration <= 9000:
			two.write(path+","+transcript+","+str(duration)+","+speaker+"\n")
		if totalDuration <= 18000:
			five.write(path+","+transcript+","+str(duration)+","+speaker+"\n")
		if totalDuration <= 36000:
			ten.write(path+","+transcript+","+str(duration)+","+speaker+"\n")
