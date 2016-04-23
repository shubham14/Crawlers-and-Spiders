from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib2
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pandas import DataFrame, read_csv
import time
from random import *
import re

baseURL1='http://www.consumercomplaints.in/bycategory/real-estate/bypopularity'
baseURL2='http://www.consumercomplaints.in/'

choice=int(raw_input('Enter 1 for Mozilla,2 for Google Chrome : '))
if(choice==1):
    br=webdriver.Firefox()
else:
    br=webdriver.Chrome()

def formIDListFirst(url):
    l=[]
    l1=[]
    r=requests.get(url)
    s=bs(r.text)
    for tag in s.find_all('div'):
        l.append(str(tag.get('id')))
    for ele in l:
        if ele[:1]=='c':
            l1.append(ele)
    return l1

def URLListFirst(url):
    U=[]
    br.get(url)
    l=formIDListFirst(url)
    for ele in l:
        res='//*[@id="'+ele[0]+'mcc'+ele[1:]+'"]'
        a=br.find_elements_by_xpath(res)
        for tag in a:
            title=tag.get_attribute('href')
            U.append(str(title))
    return U

def TitleList(url):
    title=[]
    br.get(url)
    res='//*[@id="allcontent"]/div[4]/div[1]/div/div[1]/div/table[1]/tbody/tr[1]/td/h1'
    a=br.find_elements_by_xpath(res)
    for tag in a:
        t=tag.text.encode('utf8')
        title.append(t)
    return title


def NameList(url):
    name=[]
    br.get(url)
    l=formIDListFirst(url)
    for ele in l:
        res='//*[@id="'+ele+'"]/table/tbody/tr[1]/td/div/div[2]/a'
        a=br.find_elements_by_xpath(res)
        for tag in a:
            t=tag.text.encode('utf8')
            name.append(t)
    return name

def DateList(url):
    date=[]
    br.get(url)
    l=formIDListFirst(url)
    for ele in l:
        res='//*[@id="'+ele+'"]/table/tbody/tr[1]/td/div/div[2]/span'
        a=br.find_elements_by_xpath(res)
        for tag in a:
            t=tag.text.encode('utf8')
            date.append(t)
    return date

def ContentList(url):
    content=[]
    br.get(url)
    l=formIDListFirst(url)
    for ele in l:
        res='//*[@id="'+ele+'"]/table/tbody/tr[3]/td/div/h3'
        a=br.find_elements_by_xpath(res)
        for tag in a:
            t=tag.text.encode('utf8')
            content.append(t)
    return content

def CommentList(url):
    content=[]
    br.get(url)
    l=formIDListFirst(url)
    for ele in l:
        res='//*[@id="'+ele+'"]/table/tbody/tr[3]/td/div'
        a=br.find_elements_by_xpath(res)
        for tag in a:
            t=tag.text.encode('utf8')
            content.append(t)
    return content

l1=[]
l2=[]
l3=[]
l4=[]
l=URLListFirst(baseURL1)
for ele in l:
    l5=TitleList(ele)
    l1.append(l5)
    l6=NameList(ele)
    l2.append(l6)
    l7=DateList(ele)
    l3.append(l5)
    l8=ContentList(ele)
    l4.append(l5)
    
list1=list(zip(l1,l2,l3,l4))
df=pd.DataFrame(data=list1,columns=['Title','Names','Date of Publication','Content or Complaint'])
df.to_csv('ComplaintsResults.csv',index=False,header=True)   
