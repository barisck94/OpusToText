import os
import speech_recognition as sr
opus_path = input("name of the file: ")
try:
    f = open(opus_path+".txt", "x")
except:
    f = open(opus_path+".txt", "a")
    f.write("\n")
wav_path = opus_path+".wav"
opus_path = opus_path+".opus"
os.system(f'ffmpeg -i "{opus_path}" -vn "converting.wav"')
r = sr.Recognizer()
with sr.AudioFile("converting.wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio, language="tr-tr")
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
os.remove("converting.wav")
f.write(s)
f.close()
