# -*- encoding: utf-8 -*-
'''
Created on 2016年7月6日

@author: LuoPei
'''
from  GendataMiningHomework.GenerateDataSetport *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# encoding: utf-8
'''
Created on 2016年4月13日

@author: LuoPei
'''


class Apriori(object):
    def __init__(self, *args, **kwargs):
        pass
    #简单测试函数~~~
    def loadDataSet(self):
        return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    
    def createC1(self,dataSet):
        C1=[]
        for transaction in dataSet:
            for item in transaction:
                if not [item] in C1:
                    C1.insert(0, [item])
        C1.sort()  #[[1],[2],..[5]]
        return map(frozenset, C1)
    
    def scanD(self,D,CK, minSupport):
        ssCnt={}
        for tid in D:
            for can in CK:
                if can.issubset(tid):
                    if not ssCnt.has_key(can):ssCnt[can]=1
                    else: ssCnt[can]+=1
                    
        numItems=float(len(D))
        retList=[]
        supportdata={}
        for key in ssCnt.keys():
            support=ssCnt[key]/numItems
            if support >=minSupport:
                retList.insert(0, key)
            supportdata[key]=support
        return retList,supportdata
    
    def aprioriGen(self,LK,k):
        retList=[]
        lenLK=len(LK)
        for i in range(lenLK):
            for j in range(i+1,lenLK):
                L1=list(LK[i])[:k-2];L2=list(LK[j])[:k-2]
                L1.sort();L2.sort()
                if L1==L2:
                    retList.append(LK[i]|LK[j])
        return retList
    
    def apriori(self,dataSet,minSupport=0.5):
        C1=self.createC1(dataSet);
        D=map(set,dataSet)
        L1,supportData=self.scanD(D, C1, minSupport)
        L=[L1]
        k=2;
        while(len(L[k-2])>0):
            CK=self.aprioriGen(L[k-2], k);
            LK,supK=self.scanD(D, CK, minSupport)
            supportData.update(supK)
            L.append(LK)
            k=k+1
        return L,supportData
            
    def calcConf(self,freqSet,H,supportData,br1,minConf):     
        prunedH=[]
        for conseq in H:
            conf=supportData[freqSet]/supportData[freqSet-conseq]
            
            if conf>=minConf:
               # print freqSet-conseq, '-->', conseq, 'conf:',conf
                br1.append((freqSet-conseq,conseq,conf))
                prunedH.append(conseq)
        return prunedH
    
    def rulesFromConseq(self,freqSet, H, supportData, br1,minConf=0.7):
        m=len(H[0])
        #print "m:",m
        if(len(freqSet)>m+1):
            Hmp1=self.aprioriGen(H, m+1)            
            Hmp1=self.calcConf(freqSet, Hmp1, supportData, br1, minConf)
            if(len(Hmp1)>1):
                self.rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)
        
        
           
    def generateRules(self,L,supportData, minConf=0.7):
        bigRuleList=[]
        for i in range(1,len(L)):
            for freqSet in L[i]:
                H1=[frozenset([item]) for item in freqSet]
                if(i>1):
                    H1=self.calcConf(freqSet, H1, supportData, bigRuleList, minConf)#原书没有这一行，这是原书上面的一个bug
                    self.rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
                else:
                    self.calcConf(freqSet, H1, supportData, bigRuleList, minConf)
                    
                    
        return bigRuleList
    
    
    def countFrequencySet(self, L):
        total=0
        for sets in L:
            total += len(sets)
            
        return total
        
          
    def visulization(self, L, supportdata, rules,feature):
        
        #设置中文支持
        font_peipei_consolas = FontProperties(fname="STSONG.TTF")
        #根据L, supportdata 创建对应字典
        L_Support={}
        for sets in L:
            for set in sets:
                L_Support[set]=supportdata[set]  
        
        sorted_L_Support=sorted(L_Support.iteritems(),key =lambda x:x[1],reverse=True)
        sorted_rules=sorted(rules,key=lambda x:x[2],reverse=True)
        
        _,axes=plt.subplots(1, 2)
        
        freq_x=[x for x in range(len(sorted_L_Support))]
        print len(freq_x),freq_x
        freq_y=[y[1] for y in sorted_L_Support]
        print len(freq_y),freq_y
        
        rules_x=[x for x in range(len(sorted_rules))]
        rules_y=[y[2] for y in sorted_rules]
        
        
        
        #freq_yticklabels=[str([feature[s] for s in list(z[0])]) for z in sorted_L_Support]
        freq_xticklabels=[str(list(z[0])) for z in sorted_L_Support]
        rules_xticklabels =["".join([str(list(z[0])),"->",str(list(z[1]))]) for z in sorted_rules]
        
        axes[0].bar(freq_x, freq_y, color='red', align='center')
        axes[0].set_title("Frequency Set and Supports", 
                 fontsize=14)
        axes[0].set_xticks(freq_x)

        axes[0].set_xticklabels(freq_xticklabels, 
                       fontsize=14,rotation=30)
        axes[0].grid()
        
        axes[1].bar(rules_x, rules_y, color='red', align='center')
        axes[1].set_title("Frequency Set and Supports", 
                 fontsize=14)
        axes[1].set_xticks(rules_x)

        axes[1].set_xticklabels(rules_xticklabels, 
                       fontsize=14,rotation=-90)
        axes[1].grid()
        plt.savefig("Stats.png")
        plt.show()
        
      
                        
if __name__=="__main__":
    filename="diagnosis.data"
    
    feature={0:"恶心",1:"腰疼",2:"尿频",3:"尿疼",4:"尿道口疼、痒",5:"膀胱炎症",6:"肾炎的前兆"}
    dataSet=generateDataSet(filename)
    ap=Apriori()
    L,supportdata=ap.apriori(dataSet,0.3)
    print "频繁项集的条数：",ap.countFrequencySet(L[:-1])
    print "频繁项集：",L[:-1]
    print "置信度：", len(supportdata),supportdata
    rules=ap.generateRules(L,supportdata,0.7)
    print "关联规则的条数：",len(rules)
    print "关联规则是：", rules
    ap.visulization(L[:-1], supportdata, rules, feature)