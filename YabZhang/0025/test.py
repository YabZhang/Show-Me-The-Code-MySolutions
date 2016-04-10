#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
"""
读取录制好的音频，利用IBM STT来时识别内容。
"""
AUDIO_FILE = 'record.wav'

# obtain audio from the file
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# IBM STT service acounts
IBM_USERNAME = "96ffd376-7af6-42eb-9121-2bcc74f67625"
IBM_PASSWORD = "VP7hTEtouCRa"

try:
    # send requests to api
    results = r.recognize_ibm(audio,
                              language="zh-CN",
                              #show_all="True",
                              username=IBM_USERNAME,
                              password=IBM_PASSWORD)
#    print "IBM Speech to Text thinks you said :"
    print "STT results:", results
except sr.UnknownValueError:
    print "IBM Speech to Text could not understand audio"
except sr.RequestError as e:
    print "Could not request results from IBM Speech Text service;\
    {0}".format(e)
