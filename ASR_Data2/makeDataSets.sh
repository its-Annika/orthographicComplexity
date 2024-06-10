# language code

python3 makeTrainFiles.py /home/ashankwi/commonVoiceData/$1/train.tsv /home/ashankwi/commonVoiceData/$1/trainFiles/ 20 $1 
python3 makeDevAndTestFiles.py /home/ashankwi/commonVoiceData/$1/dev.tsv /home/ashankwi/commonVoiceData/$1/clips/ 30 $1 Dev 
python3 makeDevAndTestFiles.py /home/ashankwi/commonVoiceData/$1/test.tsv /home/ashankwi/commonVoiceData/$1/testFiles/ 200 $1 Test

python3 convert.py $12.5HourTrain.txt $1
python3 convert.py $15HourTrain.txt $1
python3 convert.py $110HourTrain.txt $1
python3 convert.py $11HourDev.txt $1
python3 convert.py $11HourTest.txt $1
