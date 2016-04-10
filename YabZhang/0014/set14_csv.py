#!/usr/bin/env python
# coding: utf-8

import csv, json, pprint

with open("students.txt", 'r') as txt:
    data = json.load(txt)

with open("students_csv.xls", "wb") as xls:
    spamwriter = csv.writer(xls, delimiter=' ', quotechar='|', \
                           quoting=csv.QUOTE_MINIMAL)

    for key, value in data.items():
        spamwriter.writerow([key, value[0].encode("utf8")] + value[1:])

