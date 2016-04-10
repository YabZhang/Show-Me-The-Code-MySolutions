#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt, json

with open("students.txt", "r") as f:
    data = json.load(f)
    print data

wb = xlwt.Workbook()
ws = wb.add_sheet("students")
rx = cx = 0

for key, value in data.items():
    ws.write(rx, cx, key)
    for item in value:
        cx += 1
        ws.write(rx, cx, item)
    rx += 1
    cx = 0

wb.save('students_xlwt.xls')
