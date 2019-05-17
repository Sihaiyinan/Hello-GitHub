import os
import random

xmlpath = '/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_ZF_ZQ/VOC2007/Annotations/'

xmlfiles = os.listdir(xmlpath)

train_txt = open('/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_ZF_ZQ/VOC2007/ImageSets/Main/train.txt', 'w')
test_txt = open('/home/xuwh/Detect-model/py-faster-rcnn/data/BJ_XD_ZF_ZQ/VOC2007/ImageSets/Main/test.txt', 'w')

random.shuffle(xmlfiles)

num = len(xmlfiles)
train_num = int(num * 0.7)

t = 0
for xml in xmlfiles:
    if t <= train_num:
        train_txt.write(xml[:-4] + '\n')
    else:
        test_txt.write(xml[:-4] + '\n')

    t += 1



