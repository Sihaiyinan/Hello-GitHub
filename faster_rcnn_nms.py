# -*- coding: utf-8 -*-

import os
import numpy as np


def py_cpu_nms(dets, thresh):
    """Pure Python NMS baseline."""
    x1 = dets[:, 2].astype(float)
    y1 = dets[:, 3].astype(float)
    x2 = dets[:, 4].astype(float)
    y2 = dets[:, 5].astype(float)
    scores = dets[:, 1].astype(float)

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]

    return keep


detfilepath = '/home/xuwh/Documents/xiaodingoriginal/project/compute_mAP/chaxiao/results/zengqiang/origin_type_none'
xmlfilespath = '/home/xuwh/Documents/xiaodingoriginal/project/compute_mAP/chaxiao/VOC2007/Annotations/'
savenmsobj = '/home/xuwh/Documents/xiaodingoriginal/project/compute_mAP/chaxiao/results/zengqiang/nms_type_none'

with open(detfilepath, 'r') as detf:
    boxes = detf.readlines()


xmlfile = os.listdir(xmlfilespath)
num_xml = len(xmlfile)

keepobj = np.array([])

for i in range(1, num_xml + 1):
    imgboxes = []
    for box in boxes:
        box = box.strip().split(',')
        if box[0] == str(i):
            imgboxes.append(box)

    imgboxes = np.array(imgboxes)
    if imgboxes.size > 0:
        keepnum = py_cpu_nms(imgboxes, 0.5)
        keepobj = np.append(keepobj, imgboxes[keepnum])

rows = np.size(keepobj)/6
keepobj.resize(rows, 6)
keepobj = keepobj.tolist()
print len(keepobj)
for obj in keepobj:
    if float(obj[1]) < 0.0:   #删除置信度低的目标框，但是发现没有什么用
        keepobj.remove(obj)
print len(keepobj)

with open(savenmsobj, 'w') as nmsf:
    for keep in keepobj:
        temp = ','.join(k for k in keep)
        nmsf.write(temp + '\n')





