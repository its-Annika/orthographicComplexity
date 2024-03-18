'''
python3 makeDevSets.py path/to/clips/folder path/to/dev/file languageCode

'''

from mutagen.mp3 import MP3
import os
import sys
import re

dataFolder = sys.argv[1]
dataFile = sys.argv[2]
langCode = sys.argv[3]

transcriptDict = {}

#read in path,transcription from tsv file
with open(dataFile) as d:
	for line in d:
		transcriptDict[line.split("\t")[1]] = re.sub("[.!?\-\"\',;:]","",line.split("\t")[2])

storage = []
hourChunk = []

time = 0

#for the audio files in the provided file,
#take the path, look up the transcription, get the length
#storage them in 1 hour chunks

for file in os.listdir(dataFolder):
	if file in transcriptDict:
		audio = MP3(dataFolder+"/"+file)
		hourChunk.append((dataFolder+"/"+file, transcriptDict[file], audio.info.length))
		time += audio.info.length

		if time >= 3600:
			storage.append(hourChunk)
			hourChunk = []
			time = 0

totalHours = len(storage)

#write testing data files, 1 hour, 2 hours, 3 hours ...

try:
	os.mkdir(langCode + "ASR_Files")
except:
	pass

for i in range(1,totalHours + 1):
	with open(langCode + "ASR_Files/" + langCode + "dev" +  str(i) + "hour.txt", "w") as file:
		file.write("path|transcript|duration\n")
		for path,transcript,duration in sum(storage[0:i], []):
			file.write(path + "|" + transcript + "|" + str(duration) + "\n") 
