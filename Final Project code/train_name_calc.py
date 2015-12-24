import numpy as np
from os import listdir
from os.path import isfile, join
import shutil

import io

filename = '/work/sm6202/ML/data/features_50_power_all_with_pca_train'
path = '/work/sm6202/ML/data/filenames_train'

f = listdir(filename)


#with open(path,'a+') as f_handle:
#with io.open(path, 'w', encoding='unicode-escape') as f1:
#    f1.writelines(line + u'\n' for line in f)

f1=open(path,'a+')
#for ele in f:
#    f1.write(ele+'\n')
for fil1 in f:
#		print fil1
#		np.savetxt(f_handle,fil1,fmt='%d')

	f1.write( str(fil1) + "\n"  )
f1.close()

f1.close()

