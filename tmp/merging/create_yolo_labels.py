import os
import csv
import shutil
import cv2
from tqdm import tqdm

# FASE = 'training'
FASE = 'testing'

SRC = os.path.join('/media','jetze','Elements','MarineNet-45k')
src_lbl = os.path.join(SRC, FASE,'label_2')
src_img = os.path.join(SRC, FASE, 'image_2')

DEST = os.path.join('/media','jetze','Elements','MarineNet-45k')
dest_lbl = os.path.join(DEST, FASE,'label_yolo')

# temp = tempfile.NamedTemporaryFile()
if not os.path.exists(dest_lbl):
    os.makedirs(dest_lbl)

# order = {4:'left',5:'top',6:'right',7:'bottom'}

for fn in tqdm(os.listdir(src_lbl)):
    f = os.path.join(src_lbl,fn)
    dest_f = os.path.join(dest_lbl,fn)
    img_path = os.path.join(src_img,fn.replace('.txt','.jpg'))
    with open(f, 'r') as csvFile_src:
        reader = csv.reader(csvFile_src, delimiter=' ')
        img = cv2.imread(img_path)
        y, x, _ = img.shape
        with open(dest_f, 'w') as csvFile_dest:
            writer = csv.writer(csvFile_dest, delimiter=' ')
            for row in reader:
                for r in range(4,8):
                    row[r] = float(row[r])
                x_center = .5*(row[4]+row[6])/x
                y_center = .5*(row[5]+row[7])/y
                width = (row[6]-row[4])/x
                height = (row[7]-row[5])/y
                output = [0, x_center, y_center, width, height]
                writer.writerow(output)