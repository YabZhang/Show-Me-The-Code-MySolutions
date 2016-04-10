#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt, json

with open('city.txt', 'r') as f:
    data = json.load(f)
    print data

wb = xlwt.Workbook()
ws = wb.add_sheet('city')
rx = cx = 0

for key, value in data.items():
    ws.write(rx, cx, key)
    cx += 1
    ws.write(rx, cx, value)
    rx += 1
    cx = 0

wb.save("city.xls")

