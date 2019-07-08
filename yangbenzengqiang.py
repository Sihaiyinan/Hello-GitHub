# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np

def redbandchange(img):
    shape = img.shape
    temp = cv2.copyTo(img, None)
    h = shape[0]
    w = shape[1]
    for i in range(h):
        for j in range(w):
            t = img[i][j][2] + 40
            if t > 255:
                t = 255
            temp[i][j][2] = t
    return temp

def bluebandchange(img):
    shape = img.shape
    temp = cv2.copyTo(img, None)
    h = shape[0]
    w = shape[1]
    for i in range(h):
        for j in range(w):
            t = img[i][j][0] + 40
            if t > 255:
                t = 255
            temp[i][j][0] = t
    return temp

def greenbandchange(img):
    shape = img.shape
    temp = cv2.copyTo(img, None)
    h = shape[0]
    w = shape[1]
    for i in range(h):
        for j in range(w):
            t = img[i][j][1] + 40
            if t > 255:
                t = 255
            temp[i][j][1] = t
    return temp

def gaosiblur(img):
    temp = cv2.GaussianBlur(img, (5, 5), 1.6, 1.6)
    return temp

def gaosizaosheng(img):
    shape = img.shape
    temp = cv2.copyTo(img, None)
    h = shape[0]
    w = shape[1]
    for i in range(h):
        for j in range(w):
            for k in range(3):
                zs = int(np.random.normal(0, 1)*15)
                t = img[i][j][k] + zs
                if t > 255:
                    t = 255
                if t < 0:
                    t = 0
                temp[i][j][1] = t
    return temp

# def jingxiang(img):
#     shape = img.shape
#     temp = cv2.copyTo(img, None)
#     h = shape[0]
#     w = shape[1]
#     for i in range(h):
#         for j in range(w):
#             temp[i][j] = img[i][w - j - 1]
#     return temp







if __name__ == '__main__':


    nonetxtpath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/zq_project/VOC2007/noneimg'
    imagepath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/zq_project/VOC2007/JPEGImages/'
    savepath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/zq_project/VOC2007/ZQImages/'

    nonetxt = open(nonetxtpath, 'r')
    none_name = nonetxt.readlines()
    print len(none_name)

    imgnames = os.listdir(imagepath)
    count = 0
    for name in none_name:
        name = name.strip()
        if name + '.jpg' not in imgnames:
            print name
            continue

        image = cv2.imread(imagepath + name + '.jpg')

        image1 = redbandchange(image)
        cv2.imwrite(savepath + name + '_red.jpg', image1)

        image2 = bluebandchange(image)
        cv2.imwrite(savepath + name + '_blue.jpg', image2)

        image3 = greenbandchange(image)
        cv2.imwrite(savepath + name + '_green.jpg', image3)

        image4 = gaosiblur(image)
        cv2.imwrite(savepath + name + '_blur.jpg', image4)

        image5 = gaosizaosheng(image)
        cv2.imwrite(savepath + name + '_zs.jpg', image5)

        count += 1
        print count









