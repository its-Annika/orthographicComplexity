echo "t1"
python3 findVoices.py /home/ashankwi/orthographicComplexity/ASR_Data/$1ASR_Files/$11Train/audio_paths /home/ashankwi/commonVoiceData/$1/train.tsv
echo "t2.5"
python3 findVoices.py /home/ashankwi/orthographicComplexity/ASR_Data/$1ASR_Files/$12.5Train/audio_paths /home/ashankwi/commonVoiceData/$1/train.tsv
echo "T5"
python3 findVoices.py /home/ashankwi/orthographicComplexity/ASR_Data/$1ASR_Files/$15Train/audio_paths /home/ashankwi/commonVoiceData/$1/train.tsv
echo "t10"
python3 findVoices.py /home/ashankwi/orthographicComplexity/ASR_Data/$1ASR_Files/$110Train/audio_paths /home/ashankwi/commonVoiceData/$1/train.tsv

echo "test"
python3 findVoices.py /home/ashankwi/orthographicComplexity/ASR_Data/$1ASR_Files/$11Test/audio_paths /home/ashankwi/commonVoiceData/$1/test.tsv

echo "dev"
python3 findVoices.py /home/ashankwi/orthographicComplexity/ASR_Data/$1ASR_Files/$11Dev/audio_paths /home/ashankwi/commonVoiceData/$1/dev.tsv
