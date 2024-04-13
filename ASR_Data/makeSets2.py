'''
python3 makeTraingSets.py path/to/data/folder path/to/data/file languageCode task

'''

from mutagen.mp3 import MP3
import os
import sys
import re
import random

dataFolder = sys.argv[1]
dataFile = sys.argv[2]
langCode = sys.argv[3]
task = sys.argv[4]

transcriptDict = {}

#read in path,transcription from tsv file
with open(dataFile) as d:
	for line in d:
		path = line.split("\t")[1]
		transcriptDict[path] =  re.sub("[\„\“\”.\—!?\-\"\'_,;:¿¡]","",line.split("\t")[2])	
storage = []
totalTime = 0
#for the audio files in the provided file,
#take the path, look up the transcription, get the length

for file in os.listdir(dataFolder):
	if file in transcriptDict:
		audio = MP3(dataFolder+file)
		storage.append((dataFolder+file, transcriptDict[file], audio.info.length))
		totalTime += audio.info.length
		
		#don't need to go beyond 10 hour training sets for this project
		if totalTime >=  36500:
			break


random.shuffle(storage)

one = []
twoHalf = []
five = []
ten = []

time = 0
for path,transcript,duration in storage:
	time += duration

	if time <= 3600:
		one.append((path,transcript,duration))
	elif time <= 9000:
		twoHalf.append((path,transcript,duration))
	elif time <= 18000:
		five.append((path,transcript,duration))
	elif time <= 36000:
		ten.append((path,transcript,duration))


#make the directory
try:
	os.mkdir(langCode + "ASR_Files")
except:
	pass


#write the files
with open(langCode + "ASR_Files/" + langCode + "1hour" + task + ".txt", "w") as file:
	for path, transcript, duration in one:
		file.write(path + "|" + transcript + "|" + str(duration) + "\n") 

with open(langCode + "ASR_Files/" + langCode + "2.5hour" + task + ".txt", "w") as file: 
        for path, transcript, duration in twoHalf:
                file.write(path + "|" + transcript + "|" + str(duration) + "\n") 

with open(langCode + "ASR_Files/" + langCode + "5hour" + task + ".txt", "w") as file: 
        for path, transcript, duration in five:
                file.write(path + "|" + transcript + "|" + str(duration) + "\n") 

with open(langCode + "ASR_Files/" + langCode + "10hour" + task + ".txt", "w") as file: 
        for path, transcript, duration in ten:
                file.write(path + "|" + transcript + "|" + str(duration) + "\n") 
