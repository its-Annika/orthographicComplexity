
python3 makeSets2.py /home/ashankwi/commonVoiceData/$1/trainFiles/ /home/ashankwi/commonVoiceData/$1/train2.tsv  $1 Train
python3 makeSets2.py /home/ashankwi/commonVoiceData/$1/testFiles/ /home/ashankwi/commonVoiceData/$1/test2.tsv $1 Test
python3 makeSets2.py /home/ashankwi/commonVoiceData/$1/clips/ /home/ashankwi/commonVoiceData/$1/dev.tsv $1 Dev
