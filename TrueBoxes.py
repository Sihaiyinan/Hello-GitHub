#-*- coding:utf-8 -*-
# 统计图像的尺寸

import os
import xml.etree.cElementTree as ET


def read_xml(xmlpath):
    tree = ET.parse(xmlpath)
    root = tree.getroot()
    img_width = None
    img_height = None
    box_list = []
    for child_item in root:
        if child_item.tag == 'filename':
            filename = child_item.text

    for child_root in root:
        if child_root.tag == 'size':
            for child_item in child_root:
                if child_item.tag == 'width':
                    img_width = int(child_item.text)
                if child_item.tag == 'height':
                    img_height = int(child_item.text)

        if child_root.tag == 'object':
            label = None
            for child_item in child_root:
                if child_item.tag == 'name':
                    label = child_item.text
                if child_item.tag == 'bndbox':
                    tmp_box = []
                    for node in child_item:
                        tmp_box.append(int(node.text))
                    assert label is not None, 'label is none, error'
                    tmp_box.append(label)
                    box_list.append(tmp_box)


    return [filename, img_height, img_width, box_list]

xml_path = '/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/VOC2007/Annotations/'
xmls = os.listdir(xml_path)

image_size = open('/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/allboxes.txt', 'w')
for xml in xmls:
    xmlpro = read_xml(xml_path + xml)
    for pro in xmlpro[3]:
        image_size.write(str(xmlpro[0])[:-4] + ' ' + ' '.join(str(p) for p in pro[:-1]) + '\n')

image_size.close()
