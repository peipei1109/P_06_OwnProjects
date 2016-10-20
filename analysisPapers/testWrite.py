#encoding: utf-8
'''
Created on 2016年7月19日

@author: Administrator
'''
import os
import sys, shutil, string  
        
def commonFiles(src1,src2):
    src1List=[]
    src2List=[]
    for parent,dirnames,files in os.walk(src1):
        for file in files:
            
            file=os.path.splitext(file)[0] #除掉后缀名
            #print file
            src1List.append(file)
    with open("fileProcess/"+src2+".txt") as f:
        for paper_title in f.readlines():
            src2List.append(paper_title.strip())
            #print paper_title.strip()
    print len(src1List)
    print len(src2List)
    return [ i for i in src1List if i  in src2List ],[ i for i in src2List if i not in src1List ]


def commonPapers(file1,file2):
    file1List=[]
    file2List=[]
    with open(file1) as f:
        for paper_title in f.readlines():
            file1List.append(paper_title.strip())
            #print paper_title.strip()
    with open(file2) as f:
        for paper_title in f.readlines():
            file2List.append(paper_title.strip())
    print len(file1List)
    print len(file2List)
    return [ i for i in file1List if i  in file2List ]

def writeCommonFiles(commonList,desFile):
    with open("Results/"+desFile+".txt","w+") as f:
        for file in commonList:
            f.write(file+"\n")
 
def copyFile(srcPath, extractFile,desPath):
    
    extractlist=[]
    filenames = os.listdir(srcPath) #这里不能用os.walk(root)
    
    print  len(filenames)
    for filename in open(extractFile,'r').readlines():
        extractlist.append(filename.strip()+".pdf")
    print  len(extractlist)
    desPath=desPath+"/"+os.path.splitext(extractFile)[0].split("/")[1]
    if not os.path.exists(desPath+os.path.sep+os.path.splitext(extractFile)[0]):
        os.makedirs(desPath)
    for filename in filenames:
        if filename in extractlist:
            srcFile="/".join([srcPath,filename])
            destFile = desPath + os.path.sep + filename  
            if os.path.exists(srcPath) and not os.path.exists(destFile):  
                print 'cp %s %s' % (srcFile,destFile)  
                shutil.copy(srcFile,destFile)  
                
def findSubstrings(substrings,destString):
     res =  map(lambda x:str([destString.index(x),x]),filter(lambda x:x in destString,substrings))
     if res:
         return ', '.join(list(res))  
                     
def classifyPapers(srcPath,desPath):   
    #key words
    '''knowledge,entity, extraction, recommend, relation,knowlegable, extract'''
    key_list=["knowledge","entity","extraction","recommend","relation","knowlegable","extract"]
    key_list_1=["Entity","ENTITY"]
    key_list_2=["knowledge","Knowledge","KNOWLEDGE","knowlegable","Knowlegable"]
    key_list_3=["relation","Relation","RELATION"]
    key_list_4=["recognition","Recognition","RECOGNITION"]
    key=[key_list_1,key_list_2,key_list_3,key_list_4]
    fileList=[]
    filenames = os.listdir(srcPath) #这里不能用os.walk(root)
    save_f1=open(desPath+"/"+key_list_1[0],'w+')
    save_f2=open(desPath+"/"+key_list_2[0],'w+')
    save_f3=open(desPath+"/"+key_list_3[0],'w+')
    save_f4=open(desPath+"/"+key_list_4[0],'w+')
    for filename in filenames:
        filename=os.path.splitext(filename)[0]
        res1=findSubstrings(key_list_1,filename)
        res2=findSubstrings(key_list_2,filename)
        res3=findSubstrings(key_list_3,filename)
        res4=findSubstrings(key_list_4,filename)
        if res1:
            save_f1.write(filename.strip()+"\n")
        if res2:
            save_f2.write(filename.strip()+"\n")
        if res3:
            save_f3.write(filename.strip()+"\n")
        if res4:
            save_f4.write(filename.strip()+"\n")
                
    save_f1.close()
    save_f2.close()
    save_f3.close()
    save_f4.close()
    
         
        
if __name__=="__main__":
#     ret1,ret2=commonFiles("Papers","Filter_Relation")
#     print len(ret1),len(ret2)
#     writeCommonFiles(ret1,"commonRelation")
#     writeCommonFiles(ret2,"diffRelation")
#     ret =commonPapers("Filter_Entity","Filter_Knowledge")
#     writeCommonFiles(ret,"commonEntity_Knowledge")
#     ret =commonPapers("Filter_Entity","Filter_Relation")
#     writeCommonFiles(ret,"commonEntity_Relation")
#     ret =commonPapers("Filter_Knowledge","Filter_Relation")
#     writeCommonFiles(ret,"commonKnowledge_Relation")
#     srcPath="Papers"
#     extractFile="Results/commonRelation.txt"
#     desPath="ExtractPapers"
# #     copyFile(srcPath, extractFile,desPath)
#     classifyPapers(srcPath,desPath)
    ret=commonPapers("ExtractPapers/Entity","ExtractPapers/knowledge")
    writeCommonFiles(ret,"Downloads_Entity_knowledge")
    ret=commonPapers("ExtractPapers/Entity","ExtractPapers/relation")
    writeCommonFiles(ret,"Downloads_Entity_relation")
    ret=commonPapers("ExtractPapers/knowledge","ExtractPapers/relation")
    writeCommonFiles(ret,"Downloads_relation_knowledge")
    ret=commonPapers("ExtractPapers/Entity","ExtractPapers/recognition")
    writeCommonFiles(ret,"Downloads_Entity_recognition")
    ret=commonPapers("ExtractPapers/relation","ExtractPapers/recognition")
    writeCommonFiles(ret,"Downloads_relation_recognition")
    
    
    
   