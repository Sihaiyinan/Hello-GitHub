#-*- coding: utf-8 -*-
# 将xiaoding样本中的类别合并在一起

import os
import xml.dom.minidom

annpath = '/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/VOC2007/Annotations/'
annnewpath = '/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/VOC2007/newAnnotations/'
annlist = os.listdir(annpath)

print len(annlist)

for ann in annlist:
    name = ann[:-4]

    dom = xml.dom.minidom.parse(annpath + ann)
    root = dom.documentElement

    name = root.getElementsByTagName('name')
    for i in range(len(name)):
        name[i].firstChild.data = 'xiaoding'

    with open(annnewpath + ann, 'w') as f:
        dom.writexml(f)
