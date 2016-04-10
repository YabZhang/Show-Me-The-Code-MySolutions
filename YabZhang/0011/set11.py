#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def process():
    with codecs.open("filtered_words.txt", 'r', encoding="utf-8") as f:
        filtered = [item.rstrip() for item in f.readlines()]
        print filtered
        while True:
            print u"请输入词组（如：电脑）："
            get = raw_input()
            if get == r'\q': break
            if get.decode("utf8") in filtered:
                print "Freedom"
            else:
                print "Human Rights"

if __name__ == "__main__":
    process()


