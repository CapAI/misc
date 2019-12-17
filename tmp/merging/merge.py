import os
import shutil
import subprocess

import argparse

# go to src/data_object_image_2/training/
#   for f in files:
#       copy f to dest/training/image_2/
#       rename files (filename = '0000xxx.jpg' -> '1' + filename)
#       append new filename to dest/training/ train.txt '10000xxx'

# TODO validation / test set
# TODO check file name lenght, 
# 	if too short, add prefix + zeros

parser = argparse.ArgumentParser(description='Merge source dataset into destination set')
parser.add_argument('--src', dest='src', type=str, action='store',
					default='/home/jetze/datasets/MarineNet-8000', 
					help='path to source dataset')
parser.add_argument('--dest', dest='dest', type=str,action='store',
					default='/home/jetze/datasets/MarineNet-15000-boat_noboat',
					help='path to destination dataset')

args = parser.parse_args()

source_path = args.src
dest_path = args.dest

# SOURCE_PATH = os.path.join('/home','jetze','datasets','MarineNet_Beta','MarineNet','data_kitti')
# SOURCE_PATH = os.path.join('/home','jetze','datasets','tmp_source')
SOURCE_IMG = os.path.join(source_path,'training','image_2')
# SOURCE_IMG_VAL = os.path.join(SOURCE_PATH,'training','image_2')
SOURCE_LABEL = os.path.join(source_path, 'training','label_2')

# DEST_PATH = os.path.join('/home','jetze','datasets','SeaShips-kitti-test')
# DEST_PATH = os.path.join('/home','jetze','datasets','tmp_dest')
DEST_IMG = os.path.join(dest_path,'training','image_2')
DEST_LABEL = os.path.join(dest_path, 'training','label_2')

DEST_TEXT = os.path.join(dest_path, 'train.txt')

def nr_files(dir):
	n = len(os.listdir(dir))
	print(n)
	return n


# line count
def wccount(filename):
	out = subprocess.Popen(['wc', '-l', filename],
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT
			).communicate()[0]
	n = int(out.partition(b' ')[0])
	print(n)
	return n


def merge(prefix, 
			src_img,
			src_lbl,
			dest_img, 
			dest_lbl,
			dest_txt):
	new_imgs = []
	# move training photos
	for fn in os.listdir(src_img):
		if fn.endswith('.jpg') or fn.endswith('.jpeg'):
			new_fn = prefix + fn
			name_no_extension = new_fn.replace('.jpg','')
			# account for other extensions
			if fn.endswith('.jpeg'):
				new_fn = prefix + fn.replace('.jpeg','.jpg')
			if name_no_extension in new_imgs:
				print(f'Possible duplicate image: {new_fn}')
				raise Warning
			else:
				src = os.path.join(src_img, fn)
				dest = os.path.join(dest_img, new_fn)
				shutil.copy(src, dest)
				# os.rename(os.path.join(dest_img, fn),
							# os.path.join(dest_img, new_fn))
				# keep track of newly created images
				new_imgs.append(name_no_extension)

	new_lbls = []
	# move training labels
	for fn in os.listdir(src_lbl):
		if fn.endswith('.txt'):
			new_fn = prefix + fn
			name_no_extension = new_fn.replace('.txt','')	
			if name_no_extension in new_lbls:
				print(f'Possible duplicate label: {new_fn}')
				raise Warning
			else:
				src = os.path.join(src_lbl, fn)
				dest = os.path.join(dest_lbl, new_fn)
				shutil.copy(src, dest)
				# os.rename(os.path.join(dest_lbl,fn),
				# 			os.path.join(dest_lbl, new_fn) )
				new_lbls.append(name_no_extension)

	# append filename to text file
	nrs = list(set(new_imgs) & set(new_lbls))
	# TODO track images without labels

	f = open(dest_txt, 'a+t')
	for nr in nrs:
		f.write(nr+ "\r\n")
	f.close()

def compare(n_img, n_lbl, n_lines, before=True):
	if n_img == n_lbl and n_lbl == n_lines:
		print('Counts are the same')
	else:
		print('Warning: counts are NOT the same!!!')
		raise Warning


# for i, file_name in enumerate(glob.glob('*')):
# 	rename(file_name, f'{i}.txt')

if __name__ == '__main__':
	print(dest_path)

	# print('Before:')
	# n_img_before = nr_files(DEST_IMG)
	# n_lbl_before = nr_files(DEST_LABEL)
	# n_lines_before = wccount(DEST_TEXT)
	# compare(n_img_before, n_lbl_before, n_lines_before)

	# print('Merge:')
	# merge(prefix = '1',
	# 	src_img = SOURCE_IMG,
	# 	src_lbl = SOURCE_LABEL,
	# 	dest_img = DEST_IMG,
	# 	dest_lbl = DEST_LABEL,
	# 	dest_txt = DEST_TEXT)

	print('After:')
	n_img_after = nr_files(DEST_IMG)
	n_lbl_after = nr_files(DEST_LABEL)
	n_lines_after = wccount(DEST_TEXT)
	compare(n_img_after, n_lbl_after, n_lines_after)