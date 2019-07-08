# -*- coding: utf-8 -*-
# 功能 :将Faster RCNN检测出的目标框文件坐标映射到原始图像上
# 输入 :测试图像的目标框文件
# 输出 :原始图像的目标框文件



txt_path = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/source/project/results/direct/test_type_chaxiao'
save_path = '/home/xuwh/forthEPaper/TrainVaild/chaxiao/source/project/results/direct/origin_type_chaxiao'

txtfile = open(txt_path, 'r')
boxes = txtfile.readlines()

savetxt = open(save_path, 'w')

count = 0
for box in boxes:
    box = box.strip().split()
    temp = box[0].split('_')
    imgname = temp[0]

    w = int(temp[1])
    h = int(temp[2])
    bbox = list(map(float, box[2:]))
    d_x = bbox[2] - bbox[0]  # 目标框的大小，根据目标框的大小适当扩大目标框的范围，扩大边长的10%
    d_y = bbox[3] - bbox[1]
    bbox[0] += w - d_x * 0.1
    bbox[2] += w + d_x * 0.1
    bbox[1] += h - d_y * 0.1
    bbox[3] += h + d_y * 0.1
    if bbox[0] < 0:
        bbox[0] = 0
    if bbox[1] < 0:
        bbox[1] = 0

    #bbox = list(map(str, bbox))
    savetxt.write(imgname + ' ' + box[1] + ' ' + '%.2f' % bbox[0] + ' ' +'%.2f' % bbox[1] + ' '
                  + '%.2f' % bbox[2] + ' ' + '%.2f' % bbox[3] + '\n')
    count += 1
    print('{}/{}'.format(count, len(boxes)))

txtfile.close()
savetxt.close()

