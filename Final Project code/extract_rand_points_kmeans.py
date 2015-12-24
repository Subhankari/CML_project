import numpy as np
from os import listdir
from os.path import isfile, join
import time
import cProfile
import matplotlib.image as mpimg
from sklearn import preprocessing
from sklearn.decomposition import PCA

start_time = time.time()

norm1_path = '/work/sm6202/ML/data/features_100_pca_power_all_final'
f10_features = '/work/sm6202/ML/data/pca_feat_kms_all_1000_100'

i = 0
j = 0

with open(f10_features,'a+') as f_handle:

    for filename in listdir(norm1_path):
        data = np.zeros((1,75)) 
        data = np.matrix(data)
        #if i > 101:
            #break
        i = i + 1
        #print j
        j = 0
        #print filename
        #if i > 3:
        #    break
        with open(join(norm1_path,filename)) as f:
            for line in f:
                j = j + 1
                if not line.isspace():
                    floats = map(float, line.split())
                    floats = np.asarray(floats)
                    float1 = np.matrix(floats)
                    float1 = np.asarray(float1)
                    if j == 1:
                        data = float1
                    else:
                        data = np.concatenate((data,float1),axis = 0)
                
        random_10 = np.random.randint(data.shape[0], size = 1000)
        random_number = 11212015
        rng = np.random.RandomState(random_number)
        permutation1 = rng.permutation(len(random_10))
        random_10 = random_10[permutation1]
        data_10 = data[random_10]
        np.savetxt(f_handle,data_10,fmt='%.4f')
print("--- %s seconds for random_num for kmeans all 1000 100---" % (time.time() - start_time))
