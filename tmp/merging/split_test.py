import os
import random
import shutil

# SOURCE_PATH = os.path.join('/media','jetze','Elements','PASCAL-kitti-boat')
# SOURCE_PATH = os.path.join('/media','jetze','Elements','SeaShips-kitti-extra_anno')
# SOURCE_PATH = os.path.join('/media','jetze','Elements','PASCAL-3D-boat')
# SOURCE_PATH = os.path.join('/media', 'jetze','Elements','MarineNet-8000')
SOURCE_PATH = os.path.join('/media', 'jetze','Elements','OpenImagesDataset')

src_jpg = os.path.join(SOURCE_PATH,'training','image_2')
src_lbl = os.path.join(SOURCE_PATH, 'training','label_2')
src_png = os.path.join(SOURCE_PATH, 'data_object_image_2','training','image_2')

dest_jpg = os.path.join(SOURCE_PATH, 'testing','image_2')
dest_lbl = os.path.join(SOURCE_PATH, 'testing','label_2')
dest_png = os.path.join(SOURCE_PATH, 'data_object_image_2','testing','image_2')

for path in [dest_jpg, dest_lbl, dest_png]:
    if not os.path.exists(path):
        os.makedirs(path)

N_TEST = 1000

# sample images for test set
jpg_list = random.sample(os.listdir(src_jpg), N_TEST)
fns = [jpg.replace('.jpg','') for jpg in jpg_list]

for fn in fns:
    # move jpg
    src_j = os.path.join(src_jpg, fn+'.jpg')
    dest_j = os.path.join(dest_jpg, fn+'.jpg')
    shutil.move(src_j, dest_j)

    # move label
    src_l = os.path.join(src_lbl, fn+'.txt')
    dest_l = os.path.join(dest_lbl, fn+'.txt')
    try:
        shutil.move(src_l, dest_l)
    except IOError as e:
        print(f"IO error: {e}")
    # move png
    src_p = os.path.join(src_png, fn+'.png')
    dest_p = os.path.join(dest_png, fn+'.png')
    shutil.move(src_p, dest_p)