from sphfile import SPHFile
import glob
import os
import sys

dialects_path = "/fastdata/ac1zy/data/libri/LibriSpeech/dev-clean"
dialects=os.listdir(path = dialects_path)

for dialect in dialects:
    dialect_path = dialects_path + dialect
    speakers = os.listdir(path = dialect_path)
    for speaker in speakers:
        speaker_path =  os.path.join(dialect_path,speaker)        
        speaker_recordings = os.listdir(path = speaker_path)

        wav_files = glob.glob(speaker_path + '/*.WAV')

        for wav_file in wav_files:
            sph = SPHFile(wav_file)
            txt_file = ""
            txt_file = wav_file[:-3] + "TXT"

            f = open(txt_file,'r')
            for line in f:
                words = line.split(" ")
                start_time = (int(words[0])/16000)
                end_time = (int(words[1])/16000)
            print("writing file ", wav_file)
            sph.write_wav(wav_file.replace(".WAV",".wav"),start_time,end_time)  
