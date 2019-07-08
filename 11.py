#coding=utf-8

import sys
caffe_root='/home/xuwh/caffe'
sys.path.insert(0, caffe_root + '/python')

import caffe
import numpy as np

root = '/home/xuwh/Documents/rs_train_val/model/'   #根目录
deploy = root + 'VGG16/deploy.prototxt'    #deploy文件
caffe_model = root + 'train_model/solver_iter_10000.caffemodel'   #训练好的 caffemodel

net = caffe.Net(deploy, caffe_model, caffe.TEST)   #加载model和network


def Test(image_path):
   image = caffe.io.load_image(image_path)

   transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})  # 设定图片的shape格式(1,3,28,28)
   transformer.set_transpose('data', (2, 0, 1))  # 改变维度的顺序，由原始图片(28,28,3)变为(3,28,28)
   # transformer.set_mean('data', [np.mean(image[0]), np.mean(image[1]), np.mean(image[2])])    #减去均值，前面训练模型时没有减均值，这儿就不用
   transformer.set_raw_scale('data', 255)  # 缩放到【0，255】之间
   transformer.set_channel_swap('data', (2, 1, 0))  # 交换通道，将图片由RGB变为BGR

   net.blobs['data'].data[...] = transformer.preprocess('data', image)      #执行上面设置的图片预处理操作，并将图片载入到blob中

   #执行测试
   out = net.forward()
   prob= net.blobs['prob'].data[0].flatten() #取出最后一层（Softmax）属于某个类别的概率值，并打印
   order = np.argmax(prob)

   return order

img_label_path = '/home/xuwh/Documents/rs_train_val/train/test.txt'
img_path = '/home/xuwh/Documents/rs_train_val/train/allimages/'

f = open(img_label_path, 'r')
lines = f.readlines()
total_nums = len(lines)

# detect = open('/home/xuwh/Documents/rs_train_val/test/detect4.txt', 'w')

correct = 0.0
count = 0
for line in lines:
   line = line.strip().split()
   name = line[0]
   label = line[1]

   pre = Test(img_path + name)
   count += 1

   # detect.write(name + ' ' + str(pre) + '\n')

   if str(pre) == label:
      correct += 1

   print '{}/{}  correct = {}  gt | dt = {} | {}  accuracy = {:.3%}'\
      .format(count, total_nums, correct, label, str(pre), correct/count)

   # print '{}/{}'.format(count, total_nums)


