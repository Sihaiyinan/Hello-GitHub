# -*- coding: utf-8 -*-
# 功能 ：在原始图像上画出检测到的目标框
# 输入 ：原始图像， 坐标框文件
# 输出 ：画着坐标框的图像文件

import os
import cv2

imgpath = '/home/xuwh/forthEPaper/Test/twotest/bujian/VOC2007/drawimg/'
txtpath = '/home/xuwh/forthEPaper/Test/twotest/bujian/VOC2007/nonedetect'
savepath = '/home/xuwh/forthEPaper/Test/twotest/bujian/VOC2007/drawimg/'

images = os.listdir(imgpath)
txtfile = open(txtpath, 'r')
boxes = txtfile.readlines()

color = (255, 255, 0)

# 适用于图片多，box少的场景,这种方法有问题，只能读取的图像文件夹和保存的文件夹是同一个
count = 0
for box in boxes:
    box = box.strip().split(' ')
    imgname = box[0]
    if imgname + '.jpg' not in images:
        print imgname
        continue
    image = cv2.imread(imgpath + imgname + '.jpg')
    if image is None:
        print image
        continue

    bbox = map(int, map(float, box[1:]))
    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
    cv2.imwrite(savepath + imgname + '.jpg', image)
    count += 1
    print count

# #  适合于图片少，boxes多的场景
# count = 0
# for img in images:
#     image = cv2.imread(imgpath + img)
#
#     for box in boxes:
#         box = box.strip().split(' ')
#         imgname = box[0]
#         if imgname + '.jpg' != img:
#             continue
#
#         bbox = map(int, map(float, box[1:]))
#         cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
#
#     cv2.imwrite(savepath + img, image)
#     count += 1
#     print count

txtfile.close()

