#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, pprint


def static_your_code(dirpath):
    dirpath = os.path.abspath(dirpath)
    sum = {}
    for (root, dirs, files) in os.walk(dirpath):
        print root, "contains:\n"
        for file in files:
            result = {}
            if os.path.splitext(file)[-1] in ['.py', '.c', '.app']:
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        if line.strip().startswith("#"):
                            result["comments"] = result.get("comments", 0) + 1
                        elif bool(line.split()):
                            result["codes"] = result.get("codes", 0) + 1
                        elif not bool(line.split()):
                            result["blanks"] = result.get("blanks", 0) + 1
                print file, result
                for key, value in result.items():
                    sum[key] = sum.get(key, 0) + value
    return sum


if __name__ == "__main__":
    import sys, pprint
    if len(sys.argv) >= 2:
        report = static_your_code(sys.argv[1])
        pprint.pprint(report)
