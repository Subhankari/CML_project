# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
import os,sys
#from PIL import Image
from os import listdir
from os.path import isfile, join, exists
import time
import cProfile
import matplotlib.image as mpimg
from sklearn import preprocessing
#from scikit-learn import preprocessing
from sklearn.decomposition import PCA
#from scikit-learn.decomposition import PCA

f50_features = '/work/sm6202/ML/data/100_power_features_all'
#50_features2 = '/work/sm6202/ML/data/50_features2'

data = np.zeros((128))
with open(f50_features) as f:           
    i = 0
    for line in f:
#	if i == 200:
#    	    break
        floats = map(float, line.split())
        floats = np.asarray(floats)
        float1 = np.matrix(floats)
        float1 = np.asarray(float1)
        if(i == 0):
            data = float1
        else:
            data = np.concatenate((data,float1),axis = 0)
        i = i + 1
"""
with open(f50_features2) as f:
    for line in f:
        floats = map(float, line.split())
        floats = np.asarray(floats)
        float1 = np.matrix(floats)
        float1 = np.asarray(float1)
        data = np.concatenate((data,float1),axis = 0)
"""
#pca = PCA(n_components = 'mle')
pca = PCA()
pca.fit(data)
var = pca.explained_variance_
total = np.sum((var))
val = (float)(1 / total)
var = np.multiply(val,var)
sum = 0.0
num_c = 0
for i in range(var.shape[0]):
	if sum > 0.95:
		num_c = i - 1
		break
	sum += var[i]
print val
print var.shape
print np.sum((var))
print num_c
pca1 = PCA(n_components = num_c)
new_data2 = pca1.fit_transform(data)

path = '/work/sm6202/ML/data/pca_features_power_100_all'
np.savetxt((path),new_data2,fmt='%.4f')

read1_path = '/work/sm6202/ML/data/power_norm1_f1/'
read2_path = '/work/sm6202/ML/data/power_norm2_f2/'
write1_path = '/work/sm6202/ML/data/features_100_power_all_with_pca/'
i = 0
for filename in listdir(read1_path):
	data1 = np.zeros((1,128))
	data1 = np.matrix(data1)
	i = i + 1
	if exists(join(write1_path,filename)):
		continue
#	if i > 100:
#		break
	with open(join(read1_path,filename)) as f:
		data1 = np.zeros((1,128))
		data1 = np.matrix(data1)
		j = 0
		for line in f:
			j = j + 1
			if not line.isspace():
				floats = map(float, line.split())
				floats = np.asarray(floats)
				float1 = np.matrix(floats)
				float1 = np.asarray(float1)
				if j == 1:
					data1 = float1
				else:
					data1 = np.concatenate((data1,float1),axis = 0)
		new_data = pca1.transform(data1)
		print new_data.shape
		np.savetxt((join(write1_path,filename)),new_data,fmt='%.4f')
for filename in listdir(read2_path):
        data1 = np.zeros((1,128))
        data1 = np.matrix(data1)
        i = i + 1
	if exists(join(write1_path,filename)):
		continue
#       if i > 100:
#               break
        with open(join(read2_path,filename)) as f:
                data2 = np.zeros((1,128))
                data2 = np.matrix(data2)
                j = 0
                for line in f:
                        j = j + 1
                        if not line.isspace():
                                floats = map(float, line.split())
                                floats = np.asarray(floats)
                                float1 = np.matrix(floats)
                                float1 = np.asarray(float1)
                                if j == 1:
                                        data2 = float1
                                else:
                                        data2 = np.concatenate((data2,float1),axis = 0)
		new_data = pca1.transform(data2)
                print new_data.shape
                np.savetxt((join(write1_path,filename)),new_data,fmt='%.4f')
