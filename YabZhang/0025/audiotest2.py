#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyaudio, wave, time, sys

WIDTH = 2
CHANNELS = 2
RATE = 44100
FORMAT = pyaudio.paInt16
frames = []


def callback(in_data, frame_count, time_info, status):
    """
    write data into file
    """
    frames.append(in_data)
    return (in_data, pyaudio.paContinue)

def record(path="record.wav"):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   stream_callback=callback)

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


if __name__ == "__main__":
    record()
