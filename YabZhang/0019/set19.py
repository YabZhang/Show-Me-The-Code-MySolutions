#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from lxml import etree
import xlrd

def getdata(path='numbers.xls'):
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_name(path.split('.')[0])
    data = []
    for rowx in range(ws.nrows):
        data.append(ws.row_values(rowx))
    print(str(data))
    return str(data)

def genxml(data, path='numbers.xml'):
    root = etree.Element('root')

    numbers = etree.SubElement(root, 'numbers')
    numbers.append(etree.Comment(u"""数字信息\n"""))
    numbers.text = data
    root_tree = etree.ElementTree(root)
    root_tree.write(path, xml_declaration=True, pretty_print=True, encoding='utf-8')

if __name__ == '__main__':
    data = getdata()
    genxml(data)
