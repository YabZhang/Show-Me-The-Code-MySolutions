#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
"""
调用麦克风录制音频，利用IBM STT识别内容。
"""
IBM_USERNAME = "96ffd376-7af6-42eb-9121-2bcc74f67625"
IBM_PASSWORD = "VP7hTEtouCRa"

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print "Say something!"
    audio = r.listen(source, timeout=10)


try:
    # send requests to api
    results = r.recognize_ibm(audio,
                              language="zh-CN",
                              username=IBM_USERNAME,
                              password=IBM_PASSWORD)
    print "IBM Speech to Text thinks you said " + results
except sr.UnknownValueError:
    print "IBM Speech to Text could not understand audio"
except sr.RequestError as e:
    print "Could not request results from IBM Speech to Test service;\
    {0}".format(e)
