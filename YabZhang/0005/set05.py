#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os, sys

def file_filter(dirname, ip_size=[640, 1136]):
    dirname = os.path.abspath(dirname)
    filedir = os.listdir(dirname)
    for item in filedir:
        fileaddr = os.path.join(dirname, item)
        if os.path.isfile(fileaddr):
            handler(fileaddr, ip_size)

def handler(fileaddr, ip_size):
    try:
        im = Image.open(fileaddr)
        width, length= list(im.size)
    except:
        print "%s isn't a image." % fileaddr
        return

    if width>ip_size[0] or length>ip_size[1]:

        ratio_w = float(width)/ip_size[0]
        ratio_l = float(length)/ip_size[1]

        if ratio_w >= ratio_l:
           im = im.resize((ip_size[0], int(length/ratio_w)))
        else:
            im = im.resize((int(width/ratio_l), ip_size[1]))
        #im.resize((int(size[0]), int(size[1]))).save(fileaddr)
        im.save(fileaddr)
        print "%s resized !\n" % fileaddr, im.size

if __name__ == "__main__":
    if sys.argv >= 2:
        diraddr = sys.argv[1]
        file_filter(diraddr)
    else:
        print "Wrong Directory address!"


