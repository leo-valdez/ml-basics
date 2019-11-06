# -*- coding: utf-8 -*-
"""
@author: Gaurav
This code an be used to interact with the system using voice.
 The part with 'filename' can be used as the dict to store all the application that one wants to open, and then can be
 used as a reference to open the file or application.
"""
from gtts import gTTS
import os
import speech_recognition as sr
#filename={'Firefox':'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'}
r=sr.Recognizer();
with sr.Microphone() as source :
    print("Say something")
    audio=r.listen(source)
    print("time over thanks")
try:
    print("TEXT: "+r.recognize_google(audio));
    tts=gTTS(text=r.recognize_google(audio),lang='en')
    tts.save("bla.mp3")
    #os.system("bla.mp3")
    if 'Firefox' in r.recognize_google(audio):
        print("bye")
        os.startfile(os.path.join("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"))
    else:
         print('System cannot open the particular file')
except:
    pass;

