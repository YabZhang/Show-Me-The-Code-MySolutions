#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2, urllib, sys, os

def catch_pic_urls(site):
    print site
    ct = urllib2.urlopen(site).read()
    bs = BeautifulSoup(ct, 'lxml')
    urls = [url['src'] for url in bs.find_all("img", {"class": "BDE_Image"})]
    print len(urls)
    return urls

def download(url, savename):
    ct = urllib.urlopen(url).read()
    with open(savename, "wb") as f:
        f.write(ct)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        urls = catch_pic_urls(sys.argv[1]) or []
        if len(sys.argv) >= 3:
            savepath = sys.argv[2]
            if not os.path.exists(savepath):
                os.mkdir(savepath)
        if len(urls):
            print "get %d pic urls." % len(urls)
        else:
            print "No url matchs!"
        savepath = './' if not savepath else savepath
        for n, url in enumerate(urls):
            name = os.path.join(savepath, "%s_.%s" % (n, url.split('.')[-1]))
            download(url, name)
            print "%s done!" % name
    else:
        print "Wrong! At leat a site url is indeed."
