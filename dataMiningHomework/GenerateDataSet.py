# -*- encoding: utf-8 -*-
'''
Created on 2016年7月6日

@author: LuoPei
'''

def generateDataSet(file):
    dataset=[]
    with open(file,'r') as f:
        for line in f.readlines():
            line=line.strip().split("\t")[1:]
            subset=[]
            for index,item in enumerate(line):
                if item=="yes":
                    subset.append(index)
            if subset:
                dataset.append(subset)
    return   dataset      
            

if __name__=="__main__":
    
    #测试~~~
    file="diagnosis.data"
    dataset=generateDataSet(file)
    print len(dataset)
    print dataset.count([2,3,4,5]),len([x for x in dataset if 2 and 3 and 5 in x])