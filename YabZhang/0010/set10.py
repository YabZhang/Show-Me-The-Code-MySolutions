#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string, sys

class GenCheck(object):

    def __init__(self, size=(240, 60), mode="RGB", bg_color=(255,255,255)):
        self.im = Image.new(mode, size, bg_color)
        self.draw = ImageDraw.Draw(self.im)
        self.txt = None

    def gentext(self):
        self.txt = [random.choice(string.ascii_uppercase) for i in range(4)]
        print "random text: ", ''.join(self.txt)
        return self.txt

    def addbg(self):
        for w in range(self.im.size[0]):
            for h in range(self.im.size[1]):
                self.draw.point((w,h), tuple(random.randint(0, 255) for i in
                                        range(3)))
        print "Initialize photo background."

    def addtxt(self, size=30):
        font = ImageFont.truetype("Arial.ttf", size)
        print font.getsize("M")
        space = 0
        for char in self.gentext():
            space += 15
            self.draw.text((space, 15), text=char, font=font, \
                           fill=tuple(random.randint(0,255) for i in range(3)))
            space += 45

    def addfilter(self):
        self.im = self.im.filter(ImageFilter.GaussianBlur)

    def save(self, path="./sample.jpg"):
        try:
            self.im.save(path)
        except Exception:
            print sys.exc_info()

if __name__ == "__main__":
    gencheck = GenCheck()
    print "adding bg..."
    gencheck.addbg()
    print "adding strs.."
    gencheck.addtxt()
    print "adding filter of blur..."
    gencheck.addfilter()
    print "save it..."
    gencheck.save()

