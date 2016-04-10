#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import urllib2

class GetHref(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.body = False
        self.result = []

    def handle_starttag(self, tag, attrs):
        if self.body and 'href' in dict(attrs):
            temp = dict(attrs)
            if temp['href'].startswith("http"):
                self.result.append(dict(attrs).get('href'))
            return
        if tag == 'body':
            self.body = True

    def handle_endtag(self, tag):
        if tag == 'body':
            self.body = False

    def display(self):
        import pprint
        pprint.pprint(self.result)

def feeddata(url):
    if not url.startswith(r'http'):
        url = r'http://' + url
        print url
    try:
        f = urllib2.urlopen(url).read()
        print "Get HTML..."
        handler = GetHref()
        print "Initialize handler..."
        handler.feed(f)
        print "Processing data..."
        handler.display()
    except:
        print "Error!"

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        feeddata(sys.argv[1])

