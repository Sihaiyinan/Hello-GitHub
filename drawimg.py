# -*- coding: utf-8 -*-
# 功能 ：在原始图像上画出检测到的目标框
# 输入 ：原始图像， 坐标框文件
# 输出 ：画着坐标框的图像文件

import os
import cv2

imgpath = '/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_VGG/testimg/'
txtpath = '/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_VGG/chaxiao_fp'
savepath = '/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_VGG/testimg/'

images = os.listdir(imgpath)
txtfile = open(txtpath, 'r')
boxes = txtfile.readlines()

color = (255, 0, 0)

count = 0
for img in images:
    image = cv2.imread(imgpath + img)

    for box in boxes:
        box = box.strip().split(' ')
        imgname = box[0]
        if imgname + '.jpg' != img:
            continue

        bbox = map(int, map(float, box[1:]))
        cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)

    cv2.imwrite(savepath + img, image)
    count += 1
    print count

txtfile.close()

