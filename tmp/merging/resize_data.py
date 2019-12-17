import os,sys
import cv2
from tqdm import tqdm

dim = 700

# Set the directory you want to start from
rootDir = '/media/jetze/Elements/MarineNet-45k/'
phases = ['training','testing']
img_folder = 'image_2'
dest_folder = 'image_yolo'
for phase in phases:
    src_dir = os.path.join(rootDir, phase, img_folder)
    dst_dir = os.path.join(rootDir, phase, dest_folder)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for fn in tqdm(os.listdir(src_dir)):
        if fn[-4:] not in ['.jpg','.png']:
            continue
        f_path = os.path.join(src_dir, fn)
        dest_path = os.path.join(dst_dir, fn)
        img = cv2.imread(f_path)
        h, w, _ = img.shape
        if h > dim or w > dim:
            scale_h = dim/h
            scale_w = dim/w
            scale = min(scale_h,scale_w)
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        cv2.imwrite(dest_path, img)

    # for root, subdirList, fileList in os.walk(rootDir):
    #     subdirList = [d for d in dirs if d in phases]
    #     # print('Found directory: %s' % dirName)
    #     for fname in fileList:
    #         print('\t%s' % fname)
    #         # im = misc.imread(root+fname)
    #         img = cv2.imread(root+fname)

    #         sys.exit()