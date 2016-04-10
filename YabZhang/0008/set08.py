#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import sys, urllib2

class TextExtracter(HTMLParser):

    _tags = ['style', 'script']

    def __init__(self):
        HTMLParser.__init__(self)
        self.into_body = False
        self.pass_tag = None
        self.main_text = ''

    def handle_starttag(self, tag, attrs):
        if tag in self._tags:
            self.pass_tag = [True, tag]
        if tag == 'body':
            self.into_body = True

    def handle_endtag(self, tag):
        if self.pass_tag and tag==self.pass_tag[1]:
            self.pass_tag = None
        if tag == 'body':
            self.into_body = False

    def handle_data(self, data):
        if data.strip() and not self.pass_tag:
            self.main_text += (data.strip() + '\n')

    def display(self):
        print self.main_text

def gethtml(url):
    if not url.startswith(r"http"):
        url = r"http://" + url
    try:
        f = urllib2.urlopen(url)
        if f:
            print "conected!"
    except:
        print "Error!"
    print "Initialize handler...\n"
    text_extracter = TextExtracter()
    print "Start process data...\n"
    text_extracter.feed(f.read())
    text_extracter.display()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        gethtml(sys.argv[1])

