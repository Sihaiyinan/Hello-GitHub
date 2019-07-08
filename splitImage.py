# -*- coding:utf-8 -*-
# 将一张大图分成若干张小图，每一张小图之间有一定的重叠度

# import sys
import cv2
import os
# import argparse


# def parse_args():
#     """
#     Parse input arguments
#     """
#     parser = argparse.ArgumentParser(description='Divide a large picture into several small figures of the same size')
#     parser.add_argument('--img_dir', dest='img_dir', help='the path of large images',
#                         default='/home/xuwh/Documents/test/img/', type=str)
#     parser.add_argument('--save_dir', dest='save_dir', help='the path to save divided small image',
#                         default='/home/xuwh/Documents/test/result/', type=str)
#     parser.add_argument('--height', dest='height', help='the height of small image',
#                         default=800, type=int)
#     parser.add_argument('--width', dest='width', help='the width of small image',
#                         default=1000, type=int)
#     parser.add_argument('--overlap', dest='overlap', help='The overlap between two small images, (0 ~ 1)',
#                         default=0.2, type=float)
#
#     if len(sys.argv) == 1:
#         parser.print_help()
#         sys.exit(1)
#
#     args = parser.parse_args()
#     return args


def divideimage(imgs_dir, save_dir, height, width, overlap):
    rep_w = width * 0.3   # 宽度重复尺寸
    rep_h = height * 0.4  # 高度重复尺寸

    image_names = os.listdir(imgs_dir)
    num = len(image_names)

    for img in image_names:

        image = cv2.imread(imgs_dir + img)
        h, w = image.shape[0], image.shape[1]

        num -= 1
        print num

        if h < height or w < width:
            subimgname = img[0:-4] + '_0_0.jpg'
            imgsavepath = os.path.join(save_dir, subimgname)
            cv2.imwrite(imgsavepath, image)
            # print(img + ' has been processed and divided into 1 images')
            continue

        wlist = []
        hlist = []  # 存放分割的小图的坐标

        wtemp = 0
        htemp = 0

        while (True):  # 计算分割后每张小图的起始坐标，如果分割到最后不足要求的尺寸，则最后一张从底部开始算，这样正好可以完整的分割大图
            if wtemp + width < w:
                wlist.append(wtemp)
                wtemp += width - rep_w
            else:
                wlist.append(w - width)
                break

        while (True):
            if htemp + height < h:
                hlist.append(htemp)
                htemp += height - rep_h
            else:
                hlist.append(h - height)
                break

        imgnum = 0
        for wi in wlist:
            for hi in hlist:
                wi = int(wi);   hi = int(hi)
                subimg = image[hi: hi + height, wi: wi + width, :]
                subimgname = img[0:-4] + '_' + str(wi) + '_' + str(hi) + '.jpg'
                imgsavepath = os.path.join(save_dir, subimgname)
                cv2.imwrite(imgsavepath, subimg)
                imgnum += 1
        # print(img + ' has been processed and divided into ' + str(imgnum) + ' images')


if __name__ == '__main__':
    # args = parse_args()
    # print('Called with args:')
    # print(args)

    imgs_dir = '/home/xuwh/forthEPaper/Test/source/Images/'
    save_dir = '/home/xuwh/forthEPaper/Test/source/splitimgs/'
    height = 800
    width = 1000
    overlap = 0.1

    divideimage(imgs_dir, save_dir, height, width, overlap)







