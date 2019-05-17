# -*- coding: utf-8 -*-

import os
import numpy as np
import xml.etree.ElementTree as ET


def parse_rec(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        obj_struct['pose'] = obj.find('pose').text
        obj_struct['truncated'] = int(obj.find('truncated').text)
        obj_struct['difficult'] = int(obj.find('difficult').text)
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
        objects.append(obj_struct)

    return objects


detfilepath = '/home/xuwh/Documents/xiaodingoriginal/project/compute_mAP/bujian/results/origin_xiaoding'
xmlfilespath = '/home/xuwh/Documents/xiaodingoriginal/project/compute_mAP/bujian/VOC2007/Annotations/'
savenmsobj = '/home/xuwh/Documents/xiaodingoriginal/project/compute_mAP/bujian/results/nms_obj.txt'

with open(detfilepath, 'r') as detf:
    boxes = detf.readlines()


xmlfile = os.listdir(xmlfilespath)
num_xml = len(xmlfile)

keepobj = []

for i in range(1, num_xml + 1):
    imgboxes = []
    for box in boxes:
        box = box.strip().split(',')
        if box[0] == str(i):
            imgboxes.append(box)

    ## 找到对应图像的xml文件，读取gtbox
    imgxml = parse_rec(xmlfilespath + str(i) + '.xml')
    class_recs = {}
    R = [obj for obj in imgxml]
    bbox = np.array([x['bbox'] for x in R])

    inters = []
    if bbox.size > 0:
        for imgbox in imgboxes:
            imgbox = np.array(imgbox).astype(float)
            bbox = bbox.astype(float)
            ixmin = np.maximum(bbox[:, 0], imgbox[2])
            iymin = np.maximum(bbox[:, 1], imgbox[3])
            ixmax = np.minimum(bbox[:, 2], imgbox[4])
            iymax = np.minimum(bbox[:, 3], imgbox[5])
            iw = np.maximum(ixmax - ixmin + 1., 0.)
            ih = np.maximum(iymax - iymin + 1., 0.)
            inters.append(iw * ih)

        inters = np.array(inters)
        ind = []
        for inter in inters.T:
            ind.append(np.argmax(inter))

        # keepboxes = []
        for ii in ind:
            keepobj.append(imgboxes[ii])

with open(savenmsobj, 'w') as nmsf:
    for keep in keepobj:
        temp = ','.join(ke for ke in keep)
        nmsf.write(temp + '\n')





