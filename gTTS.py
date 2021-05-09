# -*- coding: utf-8 -*-
from gtts import gTTS
import os
from playsound import playsound 
f=open("1.txt",'r', encoding='utf-8') #remane file to read
if f.mode=='r':
    content=f.read()
    print(content)
tts =gTTS(content, tld='com.vn', lang='vi')
tts.save("out.mp3") #rename to save
#playsound("out.mp3")
f.close()