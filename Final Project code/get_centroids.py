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


f50_features = '/work/sm6202/ML/data/pca_feat_kms_1000_100'
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
kmeans = MiniBatchKMeans(n_clusters=4, init='k-means++')
kmeans.fit(data)
centroids = kmeans.cluster_centers_
centroid_path = '/work/sm6202/ML/data/centroids_1000_100_1'
np.savetxt((centroid_path),centroids,fmt='%.4f')


