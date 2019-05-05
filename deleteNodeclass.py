import os
import xml.etree.ElementTree as ET


xml_path = '/home/xuwh/Documents/xiaodingoriginal/imged/kkx_Annotation/'

xmlfiles = os.listdir(xml_path)

for xml in xmlfiles:
    tree = ET.parse(xml_path + xml)
    root = tree.getroot()

    for object in root.findall('object'):
        name = object.find('name')
        if name.text == 'type_head':
            root.remove(object)


    tree.write(xml_path + xml)

