# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 01:45:11 2015

@author: subhankari
"""

#import matplotlib.pyplot as plt
import numpy as np
import time
import cProfile
from os import listdir
from os.path import isfile, join
from sklearn import preprocessing
from sklearn import decomposition
from sklearn.cross_validation import train_test_split
from scipy.spatial.distance import cdist
from sklearn.cluster import MiniBatchKMeans


def VLAD(C,x):
   Y = cdist(x,C,metric='euclidean', p=2, V=None, VI=None, w=None)
   clust_index = np.argmin(Y,axis = 1)
   res_vec = np.zeros(x.shape[1])
   for i in range(Y.shape[1]):
	x_i = x[clust_index == i]
        x_i = np.add(x_i,np.multiply(-1,C[i]))
        x_i = np.sum((x_i),axis = 0)
        x_i = np.matrix(x_i)
        if i == 0:
            res_vec = x_i
        else:
            res_vec = np.concatenate((res_vec,x_i),axis = 1)
   return res_vec
    
def build_bof():
	f50_features = '/work/sm6202/ML/data/pca_feat_kms_500_50'
	with open(f50_features) as f:
        	data = np.zeros((1,75))
	        data = np.matrix(data)
		i = 0
	        for line in f:
        		floats = map(float, line.split())
		        floats = np.asarray(floats)
		        float1 = np.matrix(floats)
	  	        float1 = np.asarray(float1)
		        if(i == 0):
		                data = float1
		        else:
		                data = np.concatenate((data,float1),axis = 0)
		        i = i + 1
	kmeans = MiniBatchKMeans(n_clusters=100, init='k-means++', max_iter=1000, batch_size=100, verbose=0, compute_labels=True, random_state=None, tol=0.0, max_no_improvement=50, init_size=None, n_init=3, reassignment_ratio=0.01)
	kmeans.fit(data)
	centroids = kmeans.cluster_centers_
	centroid_path = '/work/sm6202/ML/data/centroids_500_1'
	np.savetxt((centroid_path),centroids,fmt='%.4f')

		#centroids = my_kmeans_new(20,400,data,200)
    
	vlad_features = '/work/sm6202/ML/data/vlad_features_500_train1'
	pca_features = '/work/sm6202/ML/data/features_50_power_all_with_pca_train'
    
	i = 0
	j = 0

	#print data
	with open(vlad_features,'a+') as f_handle:

	        for filename in listdir(pca_features):
			data = np.zeros((1,65)) 
			data = np.matrix(data)
	       		i = i + 1
	        	print j
		        j = 0
	           	print filename
		        #if i > 3:
	        	#    break
		        with open(join(pca_features,filename)) as f:
	                	for line in f:
		                    j = j + 1
		                    #if j > 1:
	        	            #    break
	                	    #print line
	        	            if not line.isspace():
		                        floats = map(float, line.split())
	        	                floats = np.asarray(floats)
	                	        float1 = np.matrix(floats)
	                  		float1 = np.asarray(float1)
		                        if j == 1:
		                            data = float1
	        	                else:
	                	            data = np.concatenate((data,float1),axis = 0)
	        	vlad_vec = VLAD(centroids,data)
		        file_n = np.zeros((1,1));
	        	file_n = np.matrix(file_n)
		        file_n[0,0] = filename
			vlad_vec = np.matrix(vlad_vec)
			sign_val = np.sign(vlad_vec)
			arr_abs = np.absolute(vlad_vec)
			arr_sqrt =  np.sqrt(arr_abs)
			vlad_vec = np.divide(arr_sqrt,vlad_vec)
			vlad_vec = np.multiply(sign_val,vlad_vec)
			vlad_vec = preprocessing.normalize(vlad_vec,norm='l2')
	                vlad_vec = np.concatenate((file_n,vlad_vec),axis = 1)
	                np.savetxt(f_handle,vlad_vec,fmt='%.4f')
    
    
build_bof()    
