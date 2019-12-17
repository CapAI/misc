import os
from xml.dom import minidom
import shutil

# import pandas as pd

PATH = '/home/jetze/datasets/PASCAL-VOC-trainval/'

# years
YEARS = ['VOC2007','VOC2008','VOC2009','VOC2010','VOC2012']

# classes
CLASSES = ['boat']

boat_selection = 'ImageSets/Main/boat_trainval.txt'
xml = 'Annotations'

def some_function():
    all_ids = set()
    for y in YEARS:
        if y == 'VOC2007':
            prefix = '2007_'
        else:
            prefix = ''
        
        id_path = os.path.join(PATH, y, boat_selection)

        ids = set()
        with open(id_path, "r") as f:
            for l in f:
                l = l.replace("  ",  " ")
                l = l.replace("\n", "")
                l = l.split(" ")
                if l[1] == '1':
                    y_id = prefix + l[0]
                    ids.add(y_id)
        # print(ids)
        print(len(ids))
        all_ids.update(ids)
        print('set: ' + str(len(all_ids)) +', diff: ' + str(len(all_ids)-len(ids)))
        # print(all_ids.difference(set(ids)))
        # print(set(ids).difference(all_ids))


def minidom_read():
    all_ids = set()
    ids_dict = dict()
    
    for y in YEARS:
        if y == 'VOC2007':
            prefix = '' # 2007_
        else:
            prefix = ''

        xml_path = os.path.join(PATH, y, xml)

        ids = set()

        for fn in os.listdir(xml_path):
            path_fn = os.path.join(xml_path, fn)
            
            doc = minidom.parse(path_fn)

            objects = doc.getElementsByTagName('object')
            for obj in objects:
                names = obj.getElementsByTagName('name')
                for name in names:
                    if name.firstChild.data =='boat':
                        filenames = doc.getElementsByTagName('filename')
                        filename = filenames[0].firstChild.data
                        y_id = prefix + filename.replace('.jpg','')
                        ids.add(y_id)
        ids_dict[y] = ids
        # print(len(ids))
        # all_ids.update(ids)
        # print('set: ' + str(len(all_ids)) +', diff: ' + str(len(all_ids)-len(ids)))

    return ids_dict

def move(ids_dict, years):
    src = '/home/jetze/datasets/PASCAL-VOC-trainval/'
    dest = '/home/jetze/datasets/PASCAL-VOC-boat/'

    for y in years:
        ids = ids_dict[y]
        print(ids)

        if y == 'VOC2007':
            prefix = '2007_'
        else:
            prefix = ''

        # annotations
        src_anno = os.path.join(src, y, xml)
        dest_anno = os.path.join(dest, xml)
        for fn in os.listdir(src_anno):
            anno = fn.replace('.xml', '')
            dest_fn = prefix + fn
            if anno in ids:
                print(anno)
                shutil.copy(os.path.join(src_anno, fn), 
                            os.path.join(dest_anno, dest_fn))
        
        # images
        src_img = os.path.join(src, y, 'JPEGImages')
        dest_img = os.path.join(dest, 'JPEGImages')
        for fn in os.listdir(src_img):
            img = fn.replace('.jpg', '')
            dest_fn = prefix + fn
            if img in ids:
                shutil.copy(os.path.join(src_img, fn), 
                            os.path.join(dest_img, dest_fn))

        

if __name__=='__main__':
    ids_dict = minidom_read()
    
    # YEARS = ['VOC2007','VOC2012']
    print(len(ids_dict))
    print(len(ids_dict['VOC2012']))
    move(ids_dict, YEARS)
    # some_function()