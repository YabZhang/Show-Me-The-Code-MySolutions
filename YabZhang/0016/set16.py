#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, xlwt

with open('numbers.txt') as f:
    data = json.load(f)

wb = xlwt.Workbook()
ws = wb.add_sheet('numbers')
rx = cx = 0

for seq in data:
    for d in seq:
        ws.write(rx, cx, d)
        cx += 1
    rx += 1
    cx = 0

wb.save('numbers.xls')
