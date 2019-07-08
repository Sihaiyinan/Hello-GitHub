import os
from xml.dom.minidom import Document
import xml.dom.minidom
import numpy as np
import cv2


from libs.constants import DEFAULT_ENCODING



XML_EXT = '.xml'
ENCODE_METHOD = DEFAULT_ENCODING


def WriterXMLFiles(filename, path, box_list, label_list, w, h, d):

    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root)

    foldername = doc.createElement("folder")
    foldername.appendChild(doc.createTextNode("JPEGImages"))
    root.appendChild(foldername)

    nodeFilename = doc.createElement('filename')
    nodeFilename.appendChild(doc.createTextNode(filename))
    root.appendChild(nodeFilename)

    pathname = doc.createElement("path")
    pathname.appendChild(doc.createTextNode("Unknown"))
    root.appendChild(pathname)

    sourcename=doc.createElement("source")

    databasename = doc.createElement("database")
    databasename.appendChild(doc.createTextNode("Unknown"))
    sourcename.appendChild(databasename)

    root.appendChild(sourcename)

    nodesize = doc.createElement('size')
    nodewidth = doc.createElement('width')
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodesize.appendChild(nodewidth)
    nodeheight = doc.createElement('height')
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodesize.appendChild(nodeheight)
    nodedepth = doc.createElement('depth')
    nodedepth.appendChild(doc.createTextNode(str(d)))
    nodesize.appendChild(nodedepth)
    root.appendChild(nodesize)

    segname = doc.createElement("segmented")
    segname.appendChild(doc.createTextNode("0"))
    root.appendChild(segname)

    for (box, label) in zip(box_list, label_list):
        nodeobject = doc.createElement('object')
        nodename = doc.createElement('name')
        nodename.appendChild(doc.createTextNode(str(label)))
        nodeobject.appendChild(nodename)

        nodename = doc.createElement('pose')
        nodename.appendChild(doc.createTextNode('Unspecified'))
        nodeobject.appendChild(nodename)

        nodename = doc.createElement('truncated')
        nodename.appendChild(doc.createTextNode(str(0)))
        nodeobject.appendChild(nodename)

        nodename = doc.createElement('difficult')
        nodename.appendChild(doc.createTextNode('0'))
        nodeobject.appendChild(nodename)

        nodebndbox = doc.createElement('bndbox')
        nodex1 = doc.createElement('xmin')
        nodex1.appendChild(doc.createTextNode(str(box[0])))
        nodebndbox.appendChild(nodex1)
        nodey1 = doc.createElement('ymin')
        nodey1.appendChild(doc.createTextNode(str(box[1])))
        nodebndbox.appendChild(nodey1)
        nodex2 = doc.createElement('xmax')
        nodex2.appendChild(doc.createTextNode(str(box[2])))
        nodebndbox.appendChild(nodex2)
        nodey2 = doc.createElement('ymax')
        nodey2.appendChild(doc.createTextNode(str(box[3])))
        nodebndbox.appendChild(nodey2)

        nodeobject.appendChild(nodebndbox)
        root.appendChild(nodeobject)
    fp = open(path + filename + '.xml', 'w')
    doc.writexml(fp, indent='\n', addindent="\t")
    fp.close()



def load_annoataion(p):
    '''
    load annotation from the text file
    :param p:
    :return:
    '''
    text_polys = []
    text_tags = []
    if not os.path.exists(p):
        return np.array(text_polys, dtype=np.float32)
    with open(p, 'r') as f:
        reader = f.readlines()
        for line in reader:
            line = line.strip().split(' ')
            label = line[-1]
            xmin, ymin, xmax, ymax = list(map(float, line[1:-1]))
            text_polys.append([xmin, ymin, xmax, ymax])
            text_tags.append(label)

        return np.array(text_polys, dtype=np.int32), np.array(text_tags, dtype=np.str)

if __name__ == "__main__":
    txt_path = '/home/xuwh/forthEPaper/Test/twotest/chaxiao/VOC2007/xmltxt/'
    xml_path = '/home/xuwh/forthEPaper/Test/twotest/chaxiao/VOC2007/Annotations/'
    img_path = '/home/xuwh/forthEPaper/Test/twotest/chaxiao/VOC2007/JPEGImages/'
    print(os.path.exists(txt_path))
    txts = os.listdir(txt_path)
    for count, t in enumerate(txts):
        boxes, labels = load_annoataion(os.path.join(txt_path, t))
        xml_name = t.replace('.txt', '.xml')
        img_name = t.replace('.txt', '.jpg')
        img = cv2.imread(os.path.join(img_path, img_name) + '.jpg')
        if img is not None:
            h, w, d = img.shape
            WriterXMLFiles(xml_name, xml_path, boxes, labels, w, h, d)

            print(count)