#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import xlrd, json
from lxml import etree

def readxls(path='students.xls'):
    data = {}
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_name(path.split('.')[0])
    for rowx in range(ws.nrows):
       row_data = ws.row_values(rowx)
       data[row_data[0]] = row_data[1:]
    print(str(data))
    return str(data)

def genxml(data, path='students.xml'):
    root = etree.Element('root')

    students = etree.SubElement(root, "students")
    students.tail = "\n"

    students.append(etree.Comment(u"""学生信息表 "id": [姓名，数学，语文，英语]"""))
    students.text = data

    root_tree = etree.ElementTree(root)
    #xml = etree.tostring(root, xml_declaration=True, pretty_print=True, encoding="utf-8")
    root_tree.write( xml_declaration=True, pretty_print=True, encoding="utf-8")

if __name__ == "__main__":
    data = readxls()
    genxml(data)
