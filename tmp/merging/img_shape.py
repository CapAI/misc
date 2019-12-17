import os
import csv
import shutil
import cv2
# from tempfile import NamedTemporaryFile

# tempfile = NamedTemporaryFile(delete=False, mode='w+t')
PHASE = 'training'

SRC = os.path.join('/media','jetze','Elements','MarineNet-45k','data_object_image_2')
src_lbl = os.path.join(SRC, PHASE,'image_2')

li = os.listdir(src_lbl)

for fn in os.listdir(src_lbl):
    f = os.path.join(src_lbl,fn)
    # dest_f = os.path.join(dest_lbl,fn)
    img = cv2.imread(f)
    
    if img.shape[1] is None:
        print(fn)
    # with open(f, 'r') as csvFile_src:
    #     reader = csv.reader(csvFile_src, delimiter=' ')
        # with open(dest_f, 'w') as csvFile_dest:
        #     writer = csv.writer(csvFile_dest, delimiter=' ')

        #     for row in reader:
        #         if row[0] != 'boat':
        #             print(row[0])
        #         row[0] = 'boat'
        #         writer.writerow(row)