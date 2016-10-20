#encoding: utf-8

'''
Created on 2016年7月18日

@author: Administrator
'''

#正则表达式
import re


regx=re.compile("[,|(|)|;|#|&]")
res ="123 456".split()
def parsePaper(file,des):
    save_f=open(des,'w+')
    with open(file) as f:
        for line in f.readlines():
            res=regx.split(line)
            for sub_res in res:
                if len(sub_res.strip().split())>5:
                    print sub_res
                    save_f.write(sub_res.strip()+"\n")
                    


def delicateProcess(src,des):
    save_f=open(des,'w+')
    with open(src) as f:
        for line in f.readlines():
            if "University" in line \
            or "Institute of Technology" in line \
            or "School of Computer Science and Technology" in line \
            or "Information Science and Technology" in line \
            or "Session " in line\
            or re.search("Level [0-9]",line)\
            or "Department of Computer Science and Technology" in line \
            or "Department of Computer Science and Engineering" in line \
            or "Research Center" in line:
               
                print "delete"
                continue
            
            line=line.replace("Title: ","")
            line =line.replace("» ","")
            rereobj = re.compile("Paper ID:\s*[0-9]+\s*-")
            reobj2=re.compile("/ [0-9]+") 
            line, number = rereobj.subn("",line)
            line, number = reobj2.subn("",line)
            save_f.write(line.strip()+"\n")
            
            
    save_f.close()
                       
def find_keyPapers(src,des):
    
    #key words
    '''knowledge,entity, extraction, recommend, relation,knowlegable, extract'''
    key_list=["knowledge","entity","extraction","recommend","relation","knowlegable","extract"]
    key_list_1=["knowledge","entity","extraction","relation","knowlegable","extract"]
    save_f=open(des,'w+')
    with open(src) as f:
        for line in f.readlines():
            res=findSubstrings(key_list_1,line.lower())
            if res:
                save_f.write(line.strip()+"\n")
                
    save_f.close()        
    
def find_knowledgePapers(src,des):
    
    #key words
    '''knowledge,entity, extraction, recommend, relation,knowlegable, extract'''
    key_list=["knowledge","entity","extraction","recommend","relation","knowlegable","extract"]
    key_list_1=["knowledge","knowlegable"]
    save_f=open(des,'w+')
    with open(src) as f:
        for line in f.readlines():
            res=findSubstrings(key_list_1,line.lower())
            if res:
                save_f.write(line.strip()+"\n")
                
    save_f.close()
def find_EntityPapers(src,des):
    
    #key words
    '''knowledge,entity, extraction, recommend, relation,knowlegable, extract'''
    key_list=["knowledge","entity","extraction","recommend","relation","knowlegable","extract"]
    key_list_1=["Entity","ENTITY"]
    save_f=open(des,'w+')
    with open(src) as f:
        for line in f.readlines():
            res=findSubstrings(key_list_1,line)
            if res:
                save_f.write(line.strip()+"\n")
                
    save_f.close()
    
    
def find_RelationPapers(src,des):
    
     #key words
    '''knowledge,entity, extraction, recommend, relation,knowlegable, extract'''
    key_list=["knowledge","entity","extraction","recommend","relation","knowlegable","extract"]
    key_list_1=["relation"]
    save_f=open(des,'w+')
    with open(src) as f:
        for line in f.readlines():
            res=findSubstrings(key_list_1,line.lower())
            if res:
                save_f.write(line.strip()+"\n")
                
    save_f.close()
    
def find_RecognitionPapers(src,des):
    
     #key words
    '''knowledge,entity, extraction, recommend, relation,knowlegable, extract'''
    key_list=["knowledge","entity","extraction","recommend","relation","knowlegable","extract"]
    key_list_1=["recognition"]
    save_f=open("fileProcess/"+des,'w+')
    with open(src) as f:
        for line in f.readlines():
            res=findSubstrings(key_list_1,line.lower())
            if res:
                save_f.write(line.strip()+"\n")
                
    save_f.close()  

def findSubstrings(substrings,destString):
     res =  map(lambda x:str([destString.index(x),x]),filter(lambda x:x in destString,substrings))
     if res:
         return ', '.join(list(res))                    

if __name__=="__main__":
#     src="Origion_3.txt"
#     des="Final_2.txt"
#     des2="Terminal.txt"
#     parsePaper(src,des)
#     delicateProcess(des,des2)
    src="fileProcess/Terminal.txt"
    des="Filter_2_key_list_1.txt"
    des1="Filter_Knowledge.txt"
    des2="Filter_Entity.txt"
    des3="Filter_Relation.txt"
    des4="Filter_Recognition.txt"
#     find_keyPapers(src,des)
#      
#     find_knowledgePapers(src,des1)
#     find_EntityPapers(src,des2)
#     find_RelationPapers(src,des3)
    find_RecognitionPapers(src,des4)
    
  