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


def BOF(C,x):
   bag_of_f_vector = np.zeros((C.shape[0]))
   calc_dist = cdist(x, C, metric='euclidean', p=2, V=None, VI=None, w=None)
   #print calc_dist
   labels = np.argmin(calc_dist,axis=1)
   #print labels
   for i in range (0,labels.shape[0]):
       bag_of_f_vector[labels[i]] =  bag_of_f_vector[labels[i]] + 1
        
    #print bag_of_f_vector
   return bag_of_f_vector
    
def build_bof():
	start_time = time.time()
	centroids_path = '/work/sm6202/ML/data/centroids_1000_100_1' 
	centroids = np.zeros((1,75))
	centroids = np.matrix(centroids)    
	j = 0
	with open(centroids_path) as c:
        	for l in c:
	            if not l.isspace():
        	        j = j + 1
               		floats = map(float, l.split())
	                floats = np.asarray(floats)
        	        float1 = np.matrix(floats)
	                float1 = np.asarray(float1)
        	        if j == 1:
                	    centroids = float1
	                else:
	                    centroids = np.concatenate((centroids,float1),axis = 0)
		#centroids = my_kmeans_new(20,400,data,200)
    
	vlad_features = '/work/sm6202/ML/data/bof1'
	pca_features = '/work/sm6202/ML/data/features_100_pca_power_all_final_test'
    
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
#		        if i > 1:
#	        		break
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
	        	vlad_vec = BOF(centroids,data)
		        file_n = np.zeros((1,1));
	        	file_n = np.matrix(file_n)
		        file_n[0,0] = filename
			vlad_vec = np.matrix(vlad_vec)
			#vlad_vec = preprocessing.normalize(vlad_vec,norm='l2')
	                vlad_vec = np.concatenate((file_n,vlad_vec),axis = 1)
	                np.savetxt(f_handle,vlad_vec,fmt='%.4f')
    
	print("--- %s seconds for random_num for kmeans all 1000 100---" % (time.time() - start_time))	
    
build_bof()    
