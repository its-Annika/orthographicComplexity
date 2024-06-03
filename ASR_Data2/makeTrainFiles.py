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

durationDict = {}
#{speakerID, totalDuration}
speakerDict = {}
#{speakerID, [(path,transcript,duration),(),(),]

with open(trainFilePath) as tf:
	next(tf)
	for line in tf:
		id = line.split("\t")[0]
		path = line.split("\t")[1]
		transcript = line.split("\t")[2]
		cleanTranscript = re.sub("[.,!?\"\'`#@$^&*\(\)\[\]]", "", transcript).lower()
		audio = MP3(audioFolderPath+path)
		duration = audio.info.length

		attributes = (audioFolderPath+path,cleanTranscript,duration)

		if id in speakerDict.keys():
			speakerDict[id].append(attributes)
			durationDict[id] += duration
		else:
			speakerDict[id] = [attributes]
			durationDict[id] = duration



#pull the files as equally as possible from the chosen number of speakers
speakerPool = sorted(durationDict, key=durationDict.get, reverse=True)[:speakerNumber+1]

totalDuration = 0

dataSet = []

speaker = 0

while totalDuration < 36000:
	if len(speakerDict[speakerPool[speaker]]) != 0:
		selected = random.choice(speakerDict[speakerPool[speaker]])
	#remove selected file to prevent duplicates
		temp = speakerDict[speakerPool[speaker]]
		temp.remove(selected)
		speakerDict[speakerPool[speaker]] = temp
		dataSet.append(selected)
		totalDuration += selected[2]

	if speaker == speakerNumber:
		speaker = 0
	else:
		speaker += 1

#print the dataFiles
totalDuration = 0
with open(langCode+"2.5HourTrain.txt", "w+") as two, open(langCode+"5HourTrain.txt", "w+") as five, open(langCode+"10HourTrain.txt", "w+") as ten:
	for path, transcript, duration in dataSet:
		totalDuration += duration
		if totalDuration < 9000:
			two.write(path+","+transcript+"\n")
		if totalDuration < 18000:
			five.write(path+","+transcript+"\n")
		if totalDuration < 36000:
			ten.write(path+","+transcript+"\n")
