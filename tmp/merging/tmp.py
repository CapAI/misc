import os
import shutil

SOURCE_PATH = os.path.join('/home','jetze','datasets','MarineNet-8000')
src_img = os.path.join(SOURCE_PATH,'training','image_2')
src_lbl = os.path.join(SOURCE_PATH, 'training','label_2')

new_imgs = []
for fn in os.listdir(src_img):
    if fn in new_imgs:
        print(f'Possible duplicate image: {fn}')
    else:
        new_imgs.append(fn.replace('.jpeg','.jpg').replace('.jpg',''))

new_lbls = []
for fn in os.listdir(src_lbl):
    if fn in new_lbls:
        print(f'Possible duplicate image: {fn}')
    else:
        new_lbls.append(fn.replace('.txt',''))

nrs = list(set(new_imgs) & set(new_lbls))

print(len(nrs))
print(len(new_imgs))

print(list( set(new_imgs)- set(new_imgs)))

excess_lbls = list( set(new_lbls)- set(new_imgs))
print(excess_lbls)
# for nr in excess_lbls:
#     fn = nr+'.txt'
#     src = os.path.join(src_lbl, fn)
#     dest = os.path.join(SOURCE_PATH, 'misc', 'label_2', fn) 
#     shutil.move(src, dest)


print(len(new_lbls))