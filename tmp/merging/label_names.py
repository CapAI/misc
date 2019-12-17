import os
import csv
import shutil
# from tempfile import NamedTemporaryFile

# tempfile = NamedTemporaryFile(delete=False, mode='w+t')
PHASE = 'training'

SRC = os.path.join('/media','jetze','Elements','MarineNet-45k')
src_lbl = os.path.join(SRC, PHASE,'label_2')

DEST = os.path.join('/media','jetze','Elements','MarineNet-45k-boat')
dest_lbl = os.path.join(DEST, PHASE,'label_2')

if not os.path.exists(dest_lbl):
    os.makedirs(dest_lbl)

for fn in os.listdir(src_lbl):
    f = os.path.join(src_lbl,fn)
    dest_f = os.path.join(dest_lbl,fn)
    with open(f, 'r') as csvFile_src:
        reader = csv.reader(csvFile_src, delimiter=' ')
        with open(dest_f, 'w') as csvFile_dest:
            writer = csv.writer(csvFile_dest, delimiter=' ')

            for row in reader:
                if row[0] != 'boat':
                    print(row[0])
                row[0] = 'boat'
                writer.writerow(row)