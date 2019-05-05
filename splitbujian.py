# -*- coding: utf-8 -*-
# 功能 ：从原始图像上切割部件
# 输入 ：原始图像， 目标框文件
# 输出 ：部件图像


import os
import cv2

srcimgpath = '/home/xuwh/Documents/xiaodingoriginal/VOCFiles/AllImages/'
txtpath = '/home/xuwh/Documents/xiaodingoriginal/imged/split_bujian/txtfile/original_bujian'
save_dir = '/home/xuwh/Documents/xiaodingoriginal/imged/split_bujian/bujian/'

srcimgs = os.listdir(srcimgpath)

txtfile = open(txtpath, 'r')
boxes = txtfile.readlines()

count = 0
for img in srcimgs:
    image = cv2.imread(srcimgpath + img)
    width = image.shape[1]
    height = image.shape[0]

    for box in boxes:
        box = box.strip().split(',')
        imgname = box[0]

        if imgname + '.jpg' != img:
            continue

        bboxint = map(int, map(float, box[2:]))

        if bboxint[2] > width:
            bboxint[2] = width
        if bboxint[3] > height:
            bboxint[3] = height

        subimg = image[bboxint[1]: bboxint[3], bboxint[0]: bboxint[2], :]
        subimgname = imgname + '_' + str(bboxint[0]) + '_' + str(bboxint[1]) + '.jpg'
        imgsavepath = os.path.join(save_dir, subimgname)
        cv2.imwrite(imgsavepath, subimg)

        count += 1
        print('{}/{}'.format(count, len(boxes)))


txtfile.close()