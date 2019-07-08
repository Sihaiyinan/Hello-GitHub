# -*- coding: utf-8 -*-
# 功能 ：从原始图像上切割部件
# 输入 ：原始图像， 目标框文件
# 输出 ：部件图像


import os
import cv2

srcimgpath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/source/sourceImg/'
txtpath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/source/origin_bj'
save_dir = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/source/split_voc/111/'

srcimgs = os.listdir(srcimgpath)

txtfile = open(txtpath, 'r')
boxes = txtfile.readlines()

namelist = []
chongfu = []
count = 0
for img in srcimgs:
    image = cv2.imread(srcimgpath + img)
    width = image.shape[1]
    height = image.shape[0]


    for box in boxes:
        bb = box
        box = box.strip().split(' ')
        imgname = box[0]

        if imgname + '.jpg' != img:
            continue

        bboxint = map(int, map(float, box[2:]))

        if bboxint[2] > width:
            bboxint[2] = width
        if bboxint[3] > height:
            bboxint[3] = height

        ww = bboxint[2] - bboxint[0]
        hh = bboxint[3] - bboxint[1]
        if ((ww / hh) > 5) or (hh/ww > 5):      ##防止切割的图片宽高比过大导致训练错误
            print bb
            continue

        subimg = image[bboxint[1]: bboxint[3], bboxint[0]: bboxint[2], :]
        subimgname = imgname + '_' + str(bboxint[0]) + '_' + str(bboxint[1]) + '.jpg'
        if subimgname not in namelist:
            namelist.append(subimgname)
        else:
            chongfu.append(subimgname)
            print subimgname
        imgsavepath = os.path.join(save_dir, subimgname)
        cv2.imwrite(imgsavepath, subimg)

        count += 1
        print('{}/{}'.format(count, len(boxes)))

for i in chongfu:
    print i

txtfile.close()