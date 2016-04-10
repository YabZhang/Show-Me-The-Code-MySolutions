#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from lxml import etree
import xlrd

def getdata(path='city.xls'):
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_name(path.split('.')[0])
    data = {}
    for rowx in range(ws.nrows):
        row_data = ws.row_values(rowx)
        data[row_data[0]] = row_data[1:]
    print(str(data))
    return str(data)

def genxml(data, path='city.xml'):
    root = etree.Element('root')

    citys = etree.SubElement(root, "citys")
    citys.append(etree.Comment(u"""城市信息\n"""))
    citys.text = data

    root_tree = etree.ElementTree(root)
    root_tree.write(path, xml_declaration=True, pretty_print=True,\
                    encoding='utf-8')

if __name__ == "__main__":
    data = getdata()
    genxml(data)
