#-*- coding:utf-8 -*-
# 统计图像的尺寸

import os
import xml.etree.cElementTree as ET


def read_xml(xmlpath):
    tree = ET.parse(xmlpath)
    root = tree.getroot()
    # img_width = None
    # img_height = None
    # label = None
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

xml_path = '/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_ZF/VOC2007/Annotations/'
xmls = os.listdir(xml_path)

image_none = open('/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_ZF/VOC2007/allnoneboxes.txt', 'w')
image_cx = open('/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_ZF/VOC2007/allcxboxes.txt', 'w')

for xml in xmls:
    xmlpro = read_xml(xml_path + xml)
    for box in xmlpro[3:]:

        if str(box[0]) == 'type_none':
            image_none.write(str(xmlpro[0])[:] + ' ' + ' '.join(pro for pro in box[1:]) + '\n')
        elif str(box[0]) == 'type_chaxiao':
            image_cx.write(str(xmlpro[0])[:] + ' ' + ' '.join(pro for pro in box[1:]) + '\n')

image_none.close()
image_cx.close()
