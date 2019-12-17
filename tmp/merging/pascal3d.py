import scipy.io as sio
import os

SOURCE_PATH = os.path.join('/media','jetze','Elements','PASCAL-3D-boat','Annotations')

src_mat = os.path.join(SOURCE_PATH,'boat_imagenet')

for fn in os.listdir(src_mat):
    path_fn = os.path.join(src_mat,fn)
    mat = sio.loadmat(path_fn)
    for i in range(len(mat['record'][0][0][1][0])):
        label = mat['record'][0][0][1][0][i][0][0]
        if label == 'boat':
            with open(os.path.join(SOURCE_PATH, fn.replace('.mat','.txt')),'a') as f:
                print(mat['record'][0][0][1][0][i][1][0])
                left, top, right, bottom = mat['record'][0][0][1][0][i][1][0] # Xmin, Ymin, Xmax, Ymax
                left = left if left>=0 else 0
                top = top if top>=0 else 0
                f.write(f'boat 0 0 0 {left} {top} {right} {bottom} 0 0 0 0 0 0 0 \n')

