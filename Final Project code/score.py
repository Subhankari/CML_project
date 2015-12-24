import matplotlib.pyplot as plt
import numpy as np
import math
import os,sys
from PIL import Image
from os import listdir
from os.path import isfile, join
import time
import cProfile
import matplotlib.image as mpimg
from sklearn import preprocessing
from sklearn import decomposition
import scipy.sparse as sps


path = '/work/sm6202/ML/data/vl2'
path_test = '/work/sm6202/ML/data/vlt2'

bof = np.zeros((1,75))
bof = np.matrix(bof)
query = np.zeros((1,75))
query = np.matrix(query)
j = 0
with open(path) as c:
    for l in c:
        if not l.isspace():
            j = j + 1
            floats = map(float, l.split())
            floats = np.asarray(floats)
            float1 = np.matrix(floats)
            float1 = np.asarray(float1)
            if j == 1:
                bof = float1
            else:
                bof = np.concatenate((bof,float1),axis = 0)
                
#print bof
query = np.zeros((1,75))
query = np.matrix(query)
j = 0
with open(path_test) as c:
    for l in c:
        if not l.isspace():
            j = j + 1
            floats = map(float, l.split())
            floats = np.asarray(floats)
            float1 = np.matrix(floats)
            float1 = np.asarray(float1)
            if j == 1:
		query = float1
            else:
		query = np.concatenate((query,float1),axis = 0)


bof = np.transpose(bof)

query = np.transpose(query)

query_names = query[0,:]
query = query[1::,:]
query = np.transpose(query)
img_names = bof[0,:]
bof = bof[1::,:]

sign_val = np.sign(bof)
abs_val = np.absolute(bof)
sqrt_val = np.sqrt(abs_val)
data = np.multiply(sign_val,sqrt_val)
v = np.linalg.norm(bof)
bof = bof / v


shape = (bof.shape[0], bof.shape[1])
sps_mat = sps.csr_matrix((bof.shape[0], bof.shape[1]))
for j in xrange(bof.shape[0]):
    r = np.zeros(bof.shape[1])
    r = np.add(r,j)
    c = np.arange(bof.shape[1])
    data = bof[j,:]
    sps_mat = sps_mat + sps.csr_matrix((data,(r,c)),shape=(bof.shape[0],bof.shape[1]))
    
shape_q = (query.shape[0], query.shape[1])
query_mat = sps.csr_matrix((query.shape[0], query.shape[1]))
for j in xrange(query.shape[0]):
    r = np.zeros(query.shape[1])
    r = np.add(r,j)
    c = np.arange(query.shape[1])
    data = query[j,:]
    query_mat = query_mat + sps.csr_matrix((data,(r,c)),shape=(query.shape[0],query.shape[1]))
    
print query_mat.shape
print sps_mat.shape
scores = query_mat * sps_mat
scores = scores.todense()

results = '/work/sm6202/ML/results/resultsbof2.dat'


with open(results,'a+') as f_handle:
    for i in range(scores.shape[0]):
        arr = np.zeros((1,1))
        arr[0,0] = query_names[i]
        #arr = query_names[i]
        #print query_names[i]
        tmp_names = img_names
        for k in range(10):
            max_val = 0.
            min_pos = 0
            for j in range (k,scores.shape[1]):
                #print j
                if scores[i,j] > max_val:
                    max_val = scores[i,j]
                    max_pos = j
            #print 'min_pos'
            #print min_pos
            temp = scores[i,k]
            scores[i,k] = scores[i,max_pos]
            scores[i,max_pos] = temp
            val = np.zeros((1,2))
            val[0,0] = k
            val[0,1] = tmp_names[max_pos]
            #print val.shape
            val = np.matrix(val)
            arr = np.concatenate((arr,val), axis = 1)
            temp = tmp_names[k]
            tmp_names[k] = tmp_names[max_pos]
            tmp_names[max_pos] = temp
        np.savetxt(f_handle,arr,fmt='%d')   
        #print arr
        
        
#print scores.shape
#print scores
    

