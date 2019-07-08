import imageio
import numpy as np


height = 1000
width = 1000

dst = np.zeros([height, width], dtype=np.uint8)

f = open('  ', 'r')
lines = f.readlines()

for line in lines:
    line = line.strip().split()
    name = line[0]
    label = line[1]
    if label == '0':
        continue


    name = name[:-4].split('_')
    x = int(name[1])
    y = height - int(name[2]) - 100

    if label == '1':
        dst[y:y+100, x:x+100] = 1
