# -*- coding: utf-8 -*-
# 删除xml中部分节点

import os
import xml.dom.minidom


ann_path = '/home/xuwh/forthEPaper/TrainVaild/bujian/project/VOC2007/Annotations/'
ann_newpath = '/home/xuwh/forthEPaper/TrainVaild/bujian/project/VOC2007/Annotations/'
ann_list = os.listdir(ann_path)

print len(ann_list)

undetectpath = '/home/xuwh/forthEPaper/TrainVaild/bujian/project/VOC2007/name'
txtfile = open(undetectpath, 'r')
unboxes = txtfile.readlines()


for ann in ann_list:
    dom = xml.dom.minidom.parse(ann_path + ann)
    root = dom.documentElement

    object = root.getElementsByTagName('object')

    for unbox in unboxes:
        unbox = unbox.strip().split()
        name = unbox[0]

        if name + '.xml' != ann:
            continue

        for i in range(len(object)):
            xmin = object[i].getElementsByTagName('xmin')[0].firstChild.data
            ymin = object[i].getElementsByTagName('ymin')[0].firstChild.data
            xmax = object[i].getElementsByTagName('xmax')[0].firstChild.data
            ymax = object[i].getElementsByTagName('ymax')[0].firstChild.data

            if xmin == unbox[1] and ymin == unbox[2] and xmax == unbox[3] and ymax == unbox[4]:
                root.removeChild(object[i])

    with open(ann_newpath + ann, 'w') as f:
        dom.writexml(f)
