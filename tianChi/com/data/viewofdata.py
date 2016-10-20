# -*- encoding: utf-8 -*-
import time
import datetime  
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from sympy.strategies.core import switch
from unittest import case


conn =mysql.connector.connect(host='127.0.0.1', database='tianchi', user='root', password='123456')
cur=conn.cursor()
store_code=[1,2,3,4,5]
Y=[{} for i in range(len(store_code))]

def createDateMap():
    d1 = datetime.datetime(2014,10,10)
    d2 = datetime.datetime(2015,12,27)
    one=datetime.timedelta(days=1)
    datedelta=(d2-d1).days+1
    print datedelta   
    
    dateDict={}
    for i in range(datedelta):
        dateDict[(d1+i*one).strftime("%Y%m%d")]=i;

    return dateDict

def loadDataSet(fileName):
    
    fr = open(fileName)
    count = len(open(fileName).readlines())#文件的行
    print count
    row=len(open(fileName).readline().strip().split('\t'))-2
    print row
    dataMat=np.zeros((count,row))
    i=0
    for line in fr.readlines():
        curLine =line.strip().split('\t')[2:]
        print 
        fltLine =map(float,curLine)
        dataMat[i,:]=fltLine
        i=i+1
    return dataMat,count


def display_specialOne_stores():
    collectSql="select store_code,date,item_id,qty_alipay,qty_alipay_njhs,pv_ipv,jhs_pv_ipv,njhs_pv_ipv,collect_uv from 01_item_store_feature where  item_id=30378;"
    for i in range(5):
        Y[i]={}
    cur.execute(collectSql)
    results=cur.fetchall()
    print results
    
        
    



def display_wholeview(dateMat,count):
    plt.plot([x for x in range(count)],dateMat[:,0],'b-',[x for x in range(count)],dateMat[:,1],'r-',[x for x in range(count)],dateMat[:,2],'k-',[x for x in range(count)],dateMat[:,3],'y-',[x for x in range(count)],dateMat[:,4],'m-',[x for x in range(count)],dateMat[:,5],'g-')
    plt.show()
    
    
if __name__=="__main__":
   
#     dataMat,count=loadDataSet("../../stat_figure2.txt")
#     display_wholeview(np.mat(dataMat),count)
    display_specialOne_stores()