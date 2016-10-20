# -*- encoding: utf-8 -*-
'''
Created on 2016年10月15日

@author: LuoPei
'''

import numpy as np
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify(inX, dataset, labels, K):
    
    #calculate distances between candidate point and dataset
    m=np.shape(dataset)[0]
    diffMat=np.tile(inX,(m,1)) -dataset
    sqdiffMat=diffMat**2
    sqdisMat=np.sum(sqdiffMat,axis=1)
    disMat=np.sqrt(sqdisMat)
    
    #sorted by arg      
    sortedDisMat=disMat.argsort()
    
    classCount={}
    
    for i in range(K):
        voteLable=labels[sortedDisMat[i]]
        
        classCount[voteLable]=classCount.get(voteLable,0)+1
        
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    
    return sortedClassCount[0][0]
        


if __name__=="__main__":
    pass