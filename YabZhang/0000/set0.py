#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

im = Image.open("avatar.jpeg")
# use a truetype font
font = ImageFont.truetype('Arial.ttf', 40)

# instanitial a draw object
draw = ImageDraw.Draw(im)
draw.text((im.size[0]-30, 10), "4", font=font, fill=(255,0,0,0))

im.show()
im.save("marked.jpeg")
