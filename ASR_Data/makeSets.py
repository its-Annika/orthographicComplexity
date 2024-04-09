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
		transcriptDict[path] =  re.sub("[\„\“\”.\—!?\-\"\',;:¿¡]","",line.split("\t")[2])	
storage = []

#for the audio files in the provided file,
#take the path, look up the transcription, get the length

for file in os.listdir(dataFolder):
	audio = MP3(dataFolder+file)
	storage.append((dataFolder+file, transcriptDict[file], audio.info.length))



random.shuffle(storage)

hourStorage = []
hourChunk = []
time = 0
for path,transcript,duration in storage:
	if file in transcriptDict:
		hourChunk.append((path,transcript,duration))
		time += duration
	
		if time >= 3600:
			hourStorage.append(hourChunk)
			hourChunk = []
			time = 0


#write testing data files, 1 hour, 2 hours, 3 hours ...

try:
	os.mkdir(langCode + "ASR_Files")
except:
	pass

for i in range(1,len(hourStorage) + 1):
	with open(langCode + "ASR_Files/" + langCode + str(i) + "hour" + task + ".txt", "w") as file:
		file.write("path|transcript|duration\n")
		for path,transcript,duration in sum(hourStorage[0:i], []):
			file.write(path + "|" + transcript + "|" + str(duration) + "\n") 
