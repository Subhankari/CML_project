# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:49:05 2015

@author: subhankari
"""


import sys,pdb
import math


def usage():
  print >> sys.stderr,"""usage: python holidays_map.py resultfile.dat

Where resultfile.dat is a textfile. Its format is:

result_file = ( result_line newline )*

# each line is a query image with associated results
result_line = query_image_name query_result*

# a query result is a pair: the result's filename is prefixed with its rank (0 based)
query_result = rank result_image_name 

Where:
- all items are separated by whitespaces (space or tab)
- image names are like 12345.jpg (case sensitive)
- the order of queries is not relevant
- if the query image is ranked, it is ignored in the scoring

Copyright INRIA 2008. License: GPL
"""
  sys.exit(1)



def score_ap_from_ranks_1 (ranks, nres):
  """ Compute the average precision of one search.
  ranks = ordered list of ranks of true positives
  nres  = total number of positives in dataset  
  """
  
  # accumulate trapezoids in PR-plot
  ap=0.0

  # All have an x-size of:
  recall_step=1.0/nres
    
  for ntp,rank in enumerate(ranks):
      
    # y-size on left side of trapezoid:
    # ntp = nb of true positives so far
    # rank = nb of retrieved items so far
    if rank==0: precision_0=1.0
    else:       precision_0=ntp/float(rank)

    # y-size on right side of trapezoid:
    # ntp and rank are increased by one
    precision_1=(ntp+1)/float(rank+1)
    
    ap+=(precision_1+precision_0)*recall_step/2.0
        
  return ap

  
def get_groundtruth():
  """ Read datafile holidays_images.dat and output a dictionary
  mapping queries to the set of positive results (plus a list of all
  images)"""
  gt={}

  """
  train_names = set()
  for line1 in open("filenames_train","r"):
      img=line1.strip()
      #print img
      train_names.add(str(img))
  """
 
  
  allnames=set()
  for line in open("holidays_images.dat","r"):
    if line == '114500.jpg':
        print line
    imname=line.strip()
    imno=int(imname[:-len(".jpg")])
    allnames.add(str(imno))
    actclass = math.ceil(imno / 100)
    actclass = int(actclass)
    #actclassval = actclass
    insclass = str(actclass)# + ".jpg"
#    imno=int(imname[:-len(".jpg")])    
    if insclass == 1145:
        print 'insclass'
        print insclass    
    if imno%100==0:
      gt_results=set()
      gt[insclass]=gt_results
     # if str(imno) in train_names:
      gt_results.add(str(imno))
    else:
      # if str(imno) in train_names:
      gt_results.add(str(imno))
      
  return (allnames,gt)

def print_perfect():
  " make a perfect result file "
  
  (allnames,gt)=get_groundtruth()
  #for qname,results in gt.iteritems():
    #print qname,
    #for rank,resname in enumerate(results):
      #print rank,resname,
    #print

def parse_results(fname):
  """ go through the results file and return them in suitable
  structures"""
  for l in open(fname,"r"):
    fields=l.split()
    query_name=fields[0]
    ranks=[int(rank) for rank in fields[1::2]]
    yield (query_name,zip(ranks,fields[2::2]))


#########################################################################
# main program

#if len(sys.argv)!=2: usage()

infilename='/home/subhankari/Desktop/Image_retrieval/project_final/results/resultsbof21.dat' #results/sys.argv[1]

(allnames,gt)=get_groundtruth()

# sum of average precisions
sum_ap=0.
# nb of images so far
n=0

# loop over result lines
for query_name,results in parse_results(infilename):
  #query_name = query_name + '.jpg'
  #print gt
  query_name=query_name.strip()
  qrno = int(query_name)  
  qryclass = math.ceil(qrno / 100)
  qryclass = int(qryclass)
  insclass = str(qryclass)
  print insclass
  #print gt
  if insclass not in gt:
    print "unknown query ",query_name
    continue 
    #sys.exit(1)

  # sort results by increasing rank
  results.sort()

  # ground truth
  gt_results=gt.pop(insclass)
  print gt_results
  if len(gt_results) > 0:
  # ranks of true positives (not including the query)
      tp_ranks=[]
    
      # apply this shift to ignore null results
      rank_shift=0
      for rank,returned_name in results:
    
        if returned_name not in allnames:
          print "image name %s not in Holidays"%returned_name
          sys.exit(1)
        #print returned_name 
        #print rank
        #print returned_name
        if returned_name==query_name:
          rank_shift=-1
          #rank_sift = 0 
        elif returned_name in gt_results:
          tp_ranks.append(rank+rank_shift)      
      #print tp_ranks 
      sum_ap+=score_ap_from_ranks_1(tp_ranks,(len(gt_results)-1))
      n+=1

"""
if gt:
  # some queries left
  print "no result for queries",gt.keys()
  sys.exit(1)
"""
print "mAP for %s: %.5f"%(infilename,sum_ap/n)

