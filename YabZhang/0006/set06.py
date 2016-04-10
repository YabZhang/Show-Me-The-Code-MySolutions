#!/usr/bin/env python
# -*- coding: utf-8 -*-

from set04 import Record
import os

common_list = ['a', 'the', 'is', 'are', 'and', 'or', 'not', 'to', 'in', 'on', 'of', 'for',
               'this', 'that', 'if', 'when', 'while', 'but', 'however']
class NewRecord(Record):
    def keyword(self, filename):
        self.preprocess(file=filename)
        temp = [(freq, word) for word, freq in self.items()]
        temp.sort(reverse=True)
        return temp[:15]

def generateReport(dirpath):
    dirpath = os.path.abspath(dirpath)
    result = []
    for file in os.listdir(dirpath):
        if os.path.splitext(file)[1] == ".txt":
            record = NewRecord()
            for (freq, word) in record.keyword(file):
                if word in common_list:
                    continue
                else:
                    result.append((os.path.split(file), word))
                    break
    print result

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        generateReport(sys.argv[1])



