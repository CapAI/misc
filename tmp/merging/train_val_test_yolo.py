import os
import random

random.seed(359244)

SRC = os.path.join('/media','jetze','Elements','MarineNet-45k')
src_img = os.path.join(SRC, 'training', 'image_yolo')
src_img_test = os.path.join(SRC, 'testing', 'image_yolo')

N_VAL = 3250
img_list = os.listdir(src_img)
val_list = random.sample(img_list, N_VAL)
val_list = [os.path.join(src_img,x)+'\n' for x in val_list]
train_list = [os.path.join(src_img,x)+'\n' for x in list(set(img_list)-set(val_list))]
test_list = [os.path.join(src_img_test, x)+'\n' for x in os.listdir(src_img_test)]

with open(os.path.join(SRC, 'train.txt'), 'w') as train:
    train.writelines(train_list)

with open(os.path.join(SRC, 'valid.txt'), 'w') as valid:
    valid.writelines(val_list)

with open(os.path.join(SRC, 'test.txt'), 'w') as test:
    test.writelines(test_list)