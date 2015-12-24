import numpy as np
from os import listdir
from os.path import isfile, join
import shutil

filename = '/work/sm6202/ML/data/features_20_pca_power_all_final'

f = listdir(filename)

#random_arr = np.arange(len(f))
#random_number = 11232015
#rng = np.random.RandomState(random_number)
#permutation = rng.permutation(len(random_arr))
#random_arr = random_arr[permutation]

#val = len(random_arr) / 2

#train = random_arr[0:val]
#test = random_arr[val:len(random_arr)]


train_files = []
test_files = []

for i in range(len(f)):
	if int(f[i]) % 100 == 0:
		train_files.append(f[i])
	else:
		test_files.append(f[i])		

#for i in train:
#    train_files.append(f[i])

#for j in test:
#    test_files.append(f[j])

path1 = '/work/sm6202/ML/data/features_20_pca_power_all_final'
train_path = '/work/sm6202/ML/data/features_20_pca_power_all_final_train'
test_path = '/work/sm6202/ML/data/features_20_pca_power_all_final_test'


i = 0
j = 0
for filename in listdir(path1):
    if filename in train_files:
        shutil.copy2((join(path1,filename)),(join(train_path,filename))) #'/dir/file.ext', '/new/dir/newname.ext')
    if filename in test_files:
        shutil.copy2((join(path1,filename)),(join(test_path,filename)))
