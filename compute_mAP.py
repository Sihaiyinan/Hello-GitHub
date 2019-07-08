#-*- coding: utf-8 -*-
import os
import numpy as np

from voc_eval import voc_eval

rootpath = '/home/xuwh/forthEPaper/Test/twotest/bujian/'

# rootpath = '/home/xuwh/forthEPaper/TrainVaild/bujian/sx_project/'
detpath = rootpath + 'results/30000/'
detfiles = os.listdir(detpath)

# classes = ('__background__',  # always index 0
#                  'simple', 'triangle', 'wings', 'cross', 'girder', 'others')
# classes = ('__background__', # always index 0
#                  'type_none', 'type_chaxiao', 'type_head')
classes = ('__background__', # always index 0
                'xiaoding')
# classes = ('__background__', # always index 0
#                   'type_none', 'type_chaxiao')


aps = []
recs = []
precs = []

annopath = os.path.join(rootpath, 'VOC2007', 'Annotations', '{:s}.xml')
imagesetfile = rootpath + 'VOC2007/ImageSets/Main/test.txt'
cachedir = rootpath + 'annotations_cache/'

for i, cls in enumerate(classes):
    if cls == '__background__':
        continue
    for f in detfiles:
        if f.find(cls) != -1:
            filename = detpath + f

    rec, prec, ap = voc_eval(
        filename, annopath, imagesetfile, cls, cachedir, ovthresh=0,
        use_07_metric=False)

    aps += [ap]
    recs += [rec[-1]]
    precs += [prec[-1]]

    print('AP for {} = {:.4f}'.format(cls, ap))
    print('recall for {} = {:.4f}'.format(cls, rec[-1]))
    print('precision for {} = {:.4f}'.format(cls, prec[-1]))

print('Mean AP = {:.4f}'.format(np.mean(aps)))
print('~~~~~~~~')

print('Results:')
for ap in aps:
    print('{:.3f}'.format(ap))
print('{:.3f}'.format(np.mean(aps)))
print('~~~~~~~~')