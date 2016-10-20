# -*- encoding: utf-8 -*-
'''
Created on 2016年10月15日

@author: LuoPei
'''
import numpy as np
from scipy.cluster.hierarchy import centroid
from numpy import Inf, nonzero




#load dataset
def loadDataSet(filename,sep):
    
    dataMat=[]
    with open(filename) as fr:
        for line in fr.realines():
            curLine=line.split(sep)
            fltline=map(float,curLine)
            dataMat.append(curLine)
    return dataMat


def disEclud(vecA,vecB):
    return np.sqrt(sum(np.power(vecA-vecB,2)))


def randCent(dataSet, k):
    
    
    n=np.shape(dataSet)[1]
    centroids=np.zeros((k,n))
    for j in xrange(n):
        minJ=min(dataSet[:,j])
        rangeJ=max(dataSet[:,j])-minJ
        centroids[:,j]=minJ+rangeJ*np.random.rand(k,1)
    return centroids



def kmeans(dataSet, k, disMeas=disEclud, createCents=randCent):

    centroids=createCents(dataSet, k)
    m=np.shape(dataSet)[0]
    clusterAssign=np.mat(np.zeros((m,2)))
    cluserChanged=True
    
    while cluserChanged:
        
        cluserChanged=False
        minDis=Inf; minIndex=-1
        for i in range(m):
            for j in range(k):
                dis=disMeas(dataSet[m,:],centroids[j,:])
                if dis<minDis:
                    minDis=dis;minIndex=j
            
            if clusterAssign[i,0]!=minIndex:
               cluserChanged=True
             
            clusterAssign[i,:]=minIndex, minDis**2
        
        
        #update centriods    
        for cent in range(k):
            ptsInClust=dataSet(nonzero(clusterAssign[:,0].A==cent)[0])
            centroids[cent,:]=np.mean(ptsInClust,axis=0)
            
    return centroids,clusterAssign
            
             
            
            
    

if __name__=="__main__":
    pass