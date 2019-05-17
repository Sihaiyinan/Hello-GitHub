# -*- coding: utf-8 -*-
# 功能： 生成每一个部件图像对应的插销的真值
# 输入： 部件图像
#       开口销在原始图像上的xml文件
#
# 输出： 每一个部件对应的txt文件，txt文件中包含该部件图像中的开口销的类别，位置

import os
import xml.etree.ElementTree as ET
import numpy as np


def parse_rec(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
        objects.append(obj_struct)

    return objects

bjpath = '/home/xuwh/Documents/xiaodingoriginal/project/bj2cx_ann/bujian.txt'
cxannpath = '/home/xuwh/Documents/xiaodingoriginal/VOCFiles/Annotations_cx/'
savepath = '/home/xuwh/Documents/xiaodingoriginal/project/bj2cx_ann/origin_cx_on_bj_txt/'

cxannfiles = os.listdir(cxannpath)

bjfile = open(bjpath, 'r')
bjlines = bjfile.readlines()

count = 0
for bj in bjlines:
    bj = bj.strip().split(',')
    bj_name = bj[0]
    bj_boxes = np.array(bj[2:]).astype(float)
    bj_txt_name = bj_name + '_' + str(int(bj_boxes[0])) + '_' + str(int(bj_boxes[1]))

    if bj_name + '.xml' not in cxannfiles:
        print bj_name
        continue

    bj_txt = open(savepath + bj_txt_name, 'w')
    cx_boxes = parse_rec(cxannpath + bj_name + '.xml')

    for cx in cx_boxes:
        # cxminx = cx['bbox'][0]
        # cxminy = cx['bbox'][1]
        # cxmaxx = cx['bbox'][2]
        # cxmaxy = cx['bbox'][3]
        BBGT = np.array(cx['bbox']).astype(float)
        label = cx['name']

        if BBGT.size > 0:
            ixmin = np.maximum(BBGT[0], bj_boxes[0])
            iymin = np.maximum(BBGT[1], bj_boxes[1])
            ixmax = np.minimum(BBGT[2], bj_boxes[2])
            iymax = np.minimum(BBGT[3], bj_boxes[3])
            iw = np.maximum(ixmax - ixmin + 1., 0.)
            ih = np.maximum(iymax - iymin + 1., 0.)
            inters = iw * ih

            ratio = inters / ((BBGT[3] - BBGT[1]) * (BBGT[2] - BBGT[0]))
            if ratio > 0.5:
                sxmin = int(ixmin - bj_boxes[0])
                symin = int(iymin - bj_boxes[1])
                if sxmin == 0:
                    sxmin += 1
                if symin == 0:
                    symin += 1
                string = [bj_txt_name, sxmin , symin, int(ixmax - bj_boxes[0]), int(iymax - bj_boxes[1])]
                bj_txt.write(' '.join(str(s) for s in string) + ' ' + label + '\n')
    bj_txt.close()
    count += 1
    print count

bjfile.close()




