import hashlib
from scipy.misc import imread, imresize, imshow
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os
def file_hash(filename):
    with open(filename,'rb') as f:
        return md5(f.read()).hexdigest()
os.getcwd()
os.chdir(r'D:\pytest')
os.getcwd()
files_list = os.listdir('.')
print (len(files_list))
duplicates=[]
hash_keys=dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]=index
        else:
            duplicates.append((index,hash_keys[filehash]))
print(duplicates)
for file_indexes in duplicates[:30]:
    try:
        plt.subplot(121),plt.imshow(imread(files_list[file_indexes[1]]))
        plt.title(file_indexes[1]),plt.xticks([]),plt.yticks([])
        plt.subplot(122),plt.imshow(imread(files_list[file_indexes[0]]))
        plt.title(str(file_indexes[0])+ 'duplicate'),plt.xticks([]),plt.yticks([])
        plt.show()
    except OSError as e:
        continue
for index in duplicates:
    os.remove(files_list[index[0]])
