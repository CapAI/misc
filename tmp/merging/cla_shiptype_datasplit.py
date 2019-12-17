import os
import random
import shutil

from tqdm import tqdm
import cv2

random.seed(359244)

DIM = 700

SRC = os.path.join('/home','jupyter','shiptype')
modes = ['train','valid','test']
n = 850
n_modes = [550, 150, 150]

mode_paths = []
for m in modes:
    mode_path = os.path.join(SRC, m)    
    mode_paths.append(mode_path)
    for type_id in [30,31,33,35,36,37,60,70,80]:
        path = os.path.join(mode_path, str(type_id))
        if not os.path.exists(path):
            os.makedirs(path)

for type_id in [30,31,33,35,36,37,60,70,80]:
    type_id = str(type_id)
    img_list = os.listdir(os.path.join(SRC, type_id))
    sample = random.sample(img_list, n)
    start = 0
    end = 0
    for mode, n_m, mode_path in zip(modes, n_modes, mode_paths):
        src_path = os.path.join(SRC, type_id)
        dest_path = os.path.join(mode_path, type_id)
        end = end + n_m
        for fn in tqdm(sample[start:end]):
            if fn[-4:] not in ['.jpg','.png']:
                continue
            src = os.path.join(src_path, fn)
            dest = os.path.join(dest_path, fn)

            img = cv2.imread(src)
            h, w, _ = img.shape
            if h > dim or w > dim:
                scale_h = dim/h
                scale_w = dim/w
                scale = min(scale_h,scale_w)
                img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            cv2.imwrite(dest, img)
            shutil.copy(src, dest)
        start = end