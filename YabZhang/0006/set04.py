#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string


class Record(dict):

    table = string.maketrans(string.punctuation, ' '*len(string.punctuation))

    def __init__(self):
        dict.__init__(self)

    def preprocess(self, file="sample.txt"):
        with open(file, 'r') as f:
            for line in f:
                temp = line.translate(self.table).split()
                self.count(temp)

    def count(self, words_list):
        for item in words_list:
            if item.isalpha():
                item = item.lower()
                self[item] = self.get(item, 0) + 1

    def display(self):
        import pprint
        pprint.pprint(self)
        print "Total %d words in this article." % len(self)

if __name__ == "__main__":
    record = Record()
    record.preprocess()
    record.display()

