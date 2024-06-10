import sys 
import os
import shutil
from pathlib import Path
import re 

#file, lang code 

file = sys.argv[1]
langCode= sys.argv[2]
storage = {}

id = 0
#get content of the lines
with open(file) as f:
	for line in f:
		storage[id] = (line.split(",")[0], line.split(",")[1])

		id += 1

#make a new directory
try:
	os.mkdir(langCode+"ASR_Files")
except:
	pass

# make new inner directory
os.mkdir(langCode+"ASR_Files"+"/"+re.sub(".txt","", file))

#write the new asr folders
#one with the id and path
#one with the id and transcript
with open(langCode+"ASR_Files"+"/"+re.sub(".txt","", file)+  "/audio_paths", "w+") as af, open(langCode+"ASR_Files"+"/"+re.sub(".txt","", file)+ "/text", "w+") as tf:
	for key in storage.keys():
		af.write(str(key) + " " + storage[key][0] + "\n")
		tf.write(str(key) + " " + storage[key][1] + "\n")


#move the inputed file to the new directory
src_path = os.path.join(os.getcwd(), file)
dst_path = os.path.join(os.getcwd(), langCode+"ASR_Files"+"/"+re.sub(".txt","", file), file)
os.rename(src_path, dst_path)






