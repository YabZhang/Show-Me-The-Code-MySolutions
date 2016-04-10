#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyaudio, wave, time, sys
import speech_recognition as sr

WIDTH = 2
CHANNELS = 2
RATE = 44100
FORMAT = pyaudio.paInt16
frames = []


def callback_record(in_data, frame_count, time_info, status):
    """
    append data into frames
    """
    frames.append(in_data)
    return (in_data, pyaudio.paContinue)

def record(path="record.wav"):
    """
    nonblock recording audio
    """
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   stream_callback=callback_record)

    stream.start_stream()

    try:
        while stream.is_active():
            get = raw_input("Type '\q' to stop:\n")
            if 'q' in get or '\q' in get:
                stream.stop_stream()
            time.sleep(0.1)
    finally:
        stream.close()
        p.terminate()

    wf = wave.open(path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return path

def recognition(audio_file='record.wav'):
    # obtain audio data from the file
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    # IBM STT service acounts
    IBM_USERNAME = "96ffd376-7af6-42eb-9121-2bcc74f67625"
    IBM_PASSWORD = "VP7hTEtouCRa"

    # handle the recognition
    try:
    # send requests to api
        result = r.recognize_ibm(audio,
                              language="zh-CN",
                              #show_all="True",
                              username=IBM_USERNAME,
                              password=IBM_PASSWORD)
        print result
        result = ''.join([char for char in result if char.strip()])
    #  print "IBM Speech to Text thinks you said :"
        print "STT result:", result, repr(result), type(result), len(result)
        execute_command(result)
    except sr.UnknownValueError:
        print "IBM Speech to Text could not understand audio"
    except sr.RequestError as e:
        print "Could not request results from IBM Speech Text service; \
                {0}".format(e)

def execute_command(command):
    import webbrowser
    if u"百度" in command:
        webbrowser.open_new(r"http://www.baidu.com")
    elif u"蝴蝶" in command:
        webbrowser.open_new(r"https://hudbt.hust.edu.cn/torrents.php")
    elif u"漫画" in command:
        webbrowser.open_new(r"http://www.ishuhui.com")

def parser(command):
    pass

if __name__ == "__main__":
    record()
    command = raw_input("If continue to do speech recognition?\n")
    if command == 'y' or command == 'yes':
        recognition()

