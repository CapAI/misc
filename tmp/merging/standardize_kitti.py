import os
import csv
import shutil
import tempfile

# FASE = 'training'
FASE = 'testing'

SRC = os.path.join('/media','jetze','Elements','PASCAL-3D-boat')
src_lbl = os.path.join(SRC, FASE,'label_2_old')

DEST = os.path.join('/media','jetze','Elements','PASCAL-3D-boat')
dest_lbl = os.path.join(DEST, FASE,'label_2')

temp = tempfile.NamedTemporaryFile()

order = {4:'left',5:'top',6:'right',7:'bottom'}

for fn in os.listdir(src_lbl):
    f = os.path.join(src_lbl,fn)
    dest_f = os.path.join(dest_lbl,fn)
    with open(f, 'r') as csvFile_src:
        reader = csv.reader(csvFile_src, delimiter=' ')
        with open(dest_f, 'w') as csvFile_dest:
            writer = csv.writer(csvFile_dest, delimiter=' ')
            for row in reader:
                if len(row)>15:
                    # print(row)
                    # print(f'row too long for: {fn}')
                    row = row[0:15]
                if row[0] not in ['boat']:
                    print(row[0])
                    print(f'label incorrected for: {fn}')
                    row[0] = 'boat'
                for i in range(1,len(row)):
                    row[i]=float(row[i])
                if row[4]>row[6]:
                    print(f'left is too far to the right: {fn}')
                    tmp = row[4]
                    row[4] = row[6]
                    row[6] = tmp
                if row[5]>row[7]:
                    # print(f'top is too far down: {fn}')
                    tmp = row[5]
                    row[5] = row[7]
                    row[7] = tmp
                for i in range(4, 8):
                    if row[i]<0:
                        print(f'{order[i]} of {fn} is negative')
                        row[i]=int(0)
                    row[i] = int(round(row[i]))
                for i in [1,2,3, 8,9,10,11,12,13,14]:
                    row[i] = int(0)
                writer.writerow(row)