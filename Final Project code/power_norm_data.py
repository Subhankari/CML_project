
# coding: utf-8

# In[34]:

#get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import math
import os,sys
from PIL import Image
from os import listdir
from os.path import isfile, join,exists
import time
import cProfile
import matplotlib.image as mpimg
from sklearn import preprocessing
from sklearn import decomposition

jpg1_path = '/work/sm6202/ML/data/jpg_features1';
jpg2_path = '/work/sm6202/ML/data/jpg_features2';
norm1_path = '/work/sm6202/ML/data/power_norm1_f1';
norm2_path = '/work/sm6202/ML/data/power_norm2_f2';

i = 0
j = 0
for filename in listdir(jpg1_path):
        if exists(join(norm1_path,filename)):
            continue
	data = np.zeros((1,128)) 
        data = np.matrix(data)
        i = i + 1
        print j
        j = 0
        #print filename
       # if i > 1:
       #     break
        with open(join(jpg1_path,filename)) as f:
            for line in f:
                j = j + 1
		print j
                #if j > 1:
                #    break
                #print line
                if not line.isspace():
                    floats = map(float, line.split())
                    #print floats
                    floats = np.asarray(floats)
                    float1 = np.matrix(floats)
                    float1 = np.asarray(float1)
                    #sign = np.sign(float1)
                    #abs_val = np.absolute(float1)
                    #print abs_val
                    #abs_val = abs_val**(0.5)
                    #float1 = np.multiply(abs_val,sign)

                    #print float1
                    if j == 1:
                        data = float1
                    else:
                        data = np.concatenate((data,float1),axis = 0)
        """
        plt.figure()
        s = np.arange(data.shape[1])
        plt.plot(s,data[1,:])
        #n, bins, patches = plt.hist(data, 50, normed=1, facecolor='g', alpha=0.75)
        print data[1]
        """
        
        
        sum = 0
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                sum = sum + (data[i,j] ** 2)
        sum = math.sqrt(math.sqrt(sum))
        data = data / sum
        
        """
        plt.figure()
        #n, bins, patches = plt.hist(data, 50, normed=1, facecolor='g', alpha=0.75)
        plt.plot(s,data[1,:])
        print data[1]
        
        """
        """
        random_200 = np.random.randint(data.shape[0], size = 50)
        random_number = 11212015
        rng = np.random.RandomState(random_number)
        permutation1 = rng.permutation(len(random_200))
        random_200 = random_200[permutation1]
        data_200 = data[random_200]
        np.savetxt(f_handle,data_200,fmt='%.4f')
        """
        np.savetxt((join(norm1_path,filename)),data,fmt='%.4f')



