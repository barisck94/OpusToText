# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 00:13:38 2023

@author: PC
"""
import os
opus_path = input("opus dosyasinin ismi: ")
try:
    f = open(opus_path+".txt", "x")
except:
    f = open(opus_path+".txt", "a")
    f.write("\n")
wav_path = opus_path+".wav"
opus_path = opus_path+".opus"
os.system(f'ffmpeg -i "{opus_path}" -vn "convertttttttttttttttttttttttttttttttttttttting.wav"')
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("convertttttttttttttttttttttttttttttttttttttting.wav") as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio, language="tr-tr")
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))
os.remove("convertttttttttttttttttttttttttttttttttttttting.wav")
f.write(s)
f.close()