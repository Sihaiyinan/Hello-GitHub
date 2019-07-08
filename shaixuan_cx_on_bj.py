# -*- coding: utf-8 -*-
# 去掉txt文件中没有内容的
import os

txtpath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/splittxt/all_txt/'
dstpath = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/splittxt/sx_txt/'

txtfile = os.listdir(txtpath)
count = 0
for txt in txtfile:
    t = open(txtpath + txt, 'r')
    tt = t.readlines()
    if(len(tt) != 0):
        print txt
        count += 1
        origin = txtpath + txt
        dst =dstpath + txt
        mingling = 'cp ' + origin + ' ' + dst
        os.system(mingling)

print count