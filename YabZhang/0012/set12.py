#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def process():
    with codecs.open("filtered_words.txt", 'r', encoding="utf8") as f:
        filtered = [item.rstrip() for item in f]
        while True:
            print "请输入任意的语句："
            get = raw_input().decode("utf8")
            if get == r'\q': break
            for item in filtered:
                if item in get:
                    get = get.replace(item, '*'*len(item))
            print "Output: ", get

if __name__ == "__main__":
    process()
