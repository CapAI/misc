import os
import shutil
import pandas as pd
import cv2

src = '/media/jetze/Elements/OpenImagesDataset/'

classes = {'boat':"/m/019jd",
            'watercraft':"/m/01rzcn",
            # 'canoe':"/m/0ph39",
            'jetski':"/m/01xs3r",
            'barge':"/m/01btn",
            'submarine':"/m/074d1"}

lbl_path = os.path.join(src,'training','label_2')
img_path = os.path.join(src,'training','image_2')
for path in [lbl_path,img_path]:
    if not os.path.exists(path):
        os.makedirs(path)

# test = pd.read_csv(os.path.join(src, 'test-annotations-bbox.csv'))
# test_id = test[test['LabelName'].isin(classes.values()) & (test.IsGroupOf == 0) & (test.IsDepiction==0) ]['ImageID'].unique()
# for fn in os.listdir(os.path.join(src, 'test')):
#     img_id = fn.replace('.jpg','')
#     if img_id in test_id:
#         # move image to
#         path_fn = os.path.join(src,'test',fn)
#         shutil.copy(path_fn, img_path)
#         # get shape of image
#         img = cv2.imread(path_fn, 1)
#         y, x, _ = img.shape
#         # make txt file
#         labels = test[test['ImageID'].isin([img_id])]
#         with open(os.path.join(lbl_path,img_id+'.txt'), 'a') as f:
#             for index, row  in labels.iterrows():
#                 if row['LabelName'] in classes.values():
#                     left = round(row.XMin * x)
#                     right = round(row.XMax * x)
#                     top = round(row.YMin * y)
#                     bottom = round(row.YMax * y)
#                     f.write(f'boat 0 0 0 {left} {top} {right} {bottom} 0 0 0 0 0 0 0 \n')
#                 else:
#                     continue


# val = pd.read_csv(os.path.join(src, 'validation-annotations-bbox.csv'))
# val_id = val[val['LabelName'].isin(classes.values()) & (val.IsGroupOf == 0) & (val.IsDepiction==0)]['ImageID'].unique()
# for fn in os.listdir(os.path.join(src, 'validation')):
#     img_id = fn.replace('.jpg','')
#     if img_id in val_id:
#         # move image to
#         path_fn = os.path.join(src,'validation',fn)
#         shutil.copy(path_fn, img_path)
#         # get shape of image
#         img = cv2.imread(path_fn, 1)
#         y, x, _ = img.shape
#         # make txt file
#         labels = val[val['ImageID'].isin([img_id])]
#         with open(os.path.join(lbl_path,img_id+'.txt'), 'a') as f:
#             for index, row  in labels.iterrows():
#                 if row['LabelName'] in classes.values():
#                     left = round(row.XMin * x)
#                     right = round(row.XMax * x)
#                     top = round(row.YMin * y)
#                     bottom = round(row.YMax * y)
#                     f.write(f'boat 0 0 0 {left} {top} {right} {bottom} 0 0 0 0 0 0 0 \n')
#                 else:
#                     continue

done = os.listdir(lbl_path)
train = pd.read_csv(os.path.join(src, 'train-annotations-bbox.csv'))
train_id = train[train['LabelName'].isin(classes.values()) & (train.IsGroupOf == 0) & (train.IsDepiction==0)]['ImageID'].unique()
for i in range(9):
    folder = 'train_0'+str(i)
    for fn in os.listdir(os.path.join(src, folder)):
        img_id = fn.replace('.jpg','')
        if img_id in train_id:
            if fn.replace('.jpg','.txt') in done:
                continue
                print('skipped')
            # move image to
            path_fn = os.path.join(src,folder,fn)
            shutil.copy(path_fn, img_path)
            # get shape of image
            img = cv2.imread(path_fn, 1)
            y, x, _ = img.shape
            # make txt file
            labels = train[train['ImageID'].isin([img_id])]
            with open(os.path.join(lbl_path,img_id+'.txt'), 'a') as f:
                for index, row  in labels.iterrows():
                    if row['LabelName'] in classes.values():
                        left = round(row.XMin * x)
                        right = round(row.XMax * x)
                        top = round(row.YMin * y)
                        bottom = round(row.YMax * y)
                        f.write(f'boat 0 0 0 {left} {top} {right} {bottom} 0 0 0 0 0 0 0 \n')
                    else:
                        continue