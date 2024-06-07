import sys 
import os
import shutil
from pathlib import Path


#file, name of new directory 

file = sys.argv[1]
newDirectory = sys.argv[2]
storage = {}

id = 0
#get content of the lines
with open(file) as f:
	next(f)
	for line in f:
		storage[id] = (line.split(",")[0], line.split(",")[1])

		id += 1

#make a new directory
try:
	os.mkdir(newDirectory)
except:
	pass


#write the new asr folders
#one with the id and path
#one with the id and transcript
with open(newDirectory + "/audio_paths", "w+") as af, open(newDirectory+ "/text", "w+") as tf:
	for key in storage.keys():
		af.write(str(key) + " " + storage[key][0] + "\n")
		tf.write(str(key) + " " + storage[key][1] + "\n")



#move the inputed file to the new directory
src_path = os.path.join(os.getcwd(), file)
dst_path = os.path.join(os.getcwd(), newDirectory, file)
os.rename(src_path, dst_path)






