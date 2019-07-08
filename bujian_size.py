#-*- coding:utf-8 -*-
# 统计部件的尺寸

import os
import xml.etree.cElementTree as ET


def read_xml(xmlpath):
    tree = ET.parse(xmlpath)
    root = tree.getroot()

    attributes = []

    filename = root.findall('filename')[0].text
    attributes.append(filename)

    size = root.findall('size')[0]
    img_width = size.findall('width')[0].text
    attributes.append(img_width)
    img_height = size.findall('height')[0].text
    attributes.append(img_height)


    for object in root.findall('object'):
        box_list = []
        label = object.find('name').text
        box_list.append(label)
        bndbox = object.find('bndbox')
        for bnd in bndbox:
            box_list.append(bnd.text)
        attributes.append(box_list)

    return attributes

xmlpath = '/home/xuwh/forthEPaper/origiNimg/VOCfiles/Annotations_bj/'
bj_txt = open('/home/xuwh/forthEPaper/origiNimg/VOCfiles/bujian.txt', 'w')

xmlfiles = os.listdir(xmlpath)
for xml in xmlfiles:
    pro = read_xml(xmlpath + xml)
    for pr in pro[3:]:
        for p in pr:
            bj_txt.write(p + ' ')
        bj_txt.write('\n')
bj_txt.close()


