#encoding: utf-8
'''
Created on 2016/7/18

@author: Administrator
'''


import urllib2
import urllib
from bs4 import BeautifulSoup
import re 
import requests
import time

 
def scrapy_Papers(srcFile,desPath):
    
    with open(srcFile) as f:
        html_list=open("html_lists.txt",'w+')
        failure_list=open("failureDownload.txt","w+")
        for paper_title in f.readlines():
            pdf_url,failure_url=scrapy_Single_Paper(paper_title.strip(),desPath)
            print pdf_url,failure_url
            html_list.write(str(pdf_url))
            html_list.write("\n")
            failure_list.write(failure_url)
            failure_list.write("\n")
            time.sleep(5)

def scrapy_Single_Paper(title,desPath): 
    '''
     test_url='http://xueshu.baidu.com/s?wd=Fast+and+Space-Efficient+Entity+Linking+in+Queries&tn=SE_baiduxueshu_c1gjeupa&cl=3&ie=utf-8&bs=Fast+and+Space-Efficient+Entity+Linking+in+Queries&f=8&rsv_bp=1&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsv_spt=3'  
   
    '''
    pdf_url=""
    failure_url=""
    opener = urllib.URLopener()
    paper_title={'wd':title}
    data = urllib.urlencode(paper_title) 
    url_0='http://xueshu.baidu.com/s?'
    url_1=data
    url_2='&tn=SE_baiduxueshu_c1gjeupa&cl=3&ie=utf-8&bs=Fast+and+Space-Efficient+Entity+Linking+in+Queries&f=8&rsv_bp=1&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsv_spt=3'
    url="".join([url_0,url_1,url_2]) 
    response = urllib2.urlopen(url)
    page = response.read()
    soap= BeautifulSoup(page)
    try:
        pdf_url=soap.find("a",href=re.compile("pdf")).get("href")
    except Exception,e:
        print "no url~~"
    print pdf_url
    print soap.title
# #     if pdf_url[0:5] !="https":
# #         pdf_url=pdf_url[0:4]+"s"+pdf_url[4:]
# #     print pdf_url
# 
    try:
        opener.retrieve(pdf_url, desPath+title+'.pdf')
    except Exception, IOError:
        print "下载失败~"
        failure_url=pdf_url
    return pdf_url,failure_url

    
    
    
    
if __name__=='__main__':
    title="Fast and Space-Efficient Entity Linking in Queries"
    desPath="Papers/"
    srcFile="rest"
    scrapy_Papers(srcFile,desPath)