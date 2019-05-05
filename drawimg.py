# -*- coding: utf-8 -*-
# 功能 ：在原始图像上画出检测到的目标框
# 输入 ：原始图像， 坐标框文件
# 输出 ：画着坐标框的图像文件

import os
import cv2

imgpath = '/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/drawmissdetect/'
txtpath = '/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/fp_chong'
savepath = '/home/xuwh/Documents/xiaodingoriginal/imged/compute_mAP/bujian/drawmissdetect/'

images = os.listdir(imgpath)
txtfile = open(txtpath, 'r')
boxes = txtfile.readlines()

color = (0, 255, 0)

count = 0
for img in images:
    image = cv2.imread(imgpath + img)

    for box in boxes:
        box = box.strip().split(' ')
        imgname = box[0]
        if imgname + '.jpg' != img:
            continue

        bbox = map(int, map(float, box[1:]))
        cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 4)

    cv2.imwrite(savepath + img, image)
    count += 1
    print count

txtfile.close()

