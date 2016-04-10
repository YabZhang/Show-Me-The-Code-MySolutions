#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

def read_file(file="keys.txt"):
    return [code.rstrip() for code in open(file, 'r')]


def set():
    r = redis.StrictRedis(host="localhost", port=6379, db=0)
    for id, code in enumerate(read_file()):
        r.set("code_%s" % id, code)
    r.save()
    print "Done!"

if __name__ == "__main__":
    set()
