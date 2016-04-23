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

baseURL1='https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:'
baseURL2='https://scholar.google.com'

choice=int(raw_input('Enter 1 for Mozilla,2 for Google Chrome : '))
if(choice==1):
    br=webdriver.Firefox()
else:
    br=webdriver.Chrome()

kword=str(raw_input('Enter keyword: '))

def formAuthorList(br,url):
    l1=[]
    br.get(url)
    links = br.find_elements_by_xpath("//*[@id='gsc_ccl']/div[*]/div[2]/h3/a")
    for link in links:
        title = link.text.encode('utf8')
        l1.append(title)
    return l1

'''def visit_URL(br,url):
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    br.get(url)
    links = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[1]/a")
    for link in links:
        title = link.text.encode('utf8')
        l1.append(title)
    links1 = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[1]/div[1]")
    for link in links1:
        title = link.text.encode('utf8')
        l2.append(title)
    links2 = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[3]/span")
    for link in links2:
        title = link.text.encode('utf8')
        l3.append(title)
    links2 = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[1]/div[2]")
    for link in links2:
        title = link.text.encode('utf8')
        l4.append(title) 
    return l1,l2,l3,l4'''

def visit_URL1(br,url):
    l9=[]
    br.get(url)
    links = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[1]/a")
    for link in links:
        title = link.text.encode('utf8')
        l9.append(title)
 #   l9=l9[:1]
    return l9

def visit_URL2(br,url):
    l10=[]
    br.get(url)
    links1 = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[1]/div[1]")
    for link in links1:
        title = link.text.encode('utf8')
        l10.append(title)
#    l10=l10[:1]
    return l10


def visit_URL3(br,url):
    l11=[]
    br.get(url)
    links2 = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[3]/span")
    for link in links2:
        title = link.text.encode('utf8')
        l11.append(title)
#    l11=l11[:1]
    return l11

def visit_URL4(br,url):
    l12=[]
    br.get(url)
    links3 = br.find_elements_by_xpath("//*[@id='gsc_a_b']/tr[*]/td[1]/div[2]")
    for link in links3:
        title = link.text.encode('utf8')
        l12.append(title)
#    l12=l12[:1]
    return l12

def formURLList(br,url):
    l13=[]
    br.get(url)
    links = br.find_elements_by_xpath("//*[@id='gsc_ccl']/div[*]/div[2]/h3/a")
    for link in links:
        url = link.get_attribute('href')
        l13.append(url)
    return l13
    
def query_split(query):
    ans=''
    l=query.split()
    for i in range(len(l)-1):
        ans+=l[i]+'_'
    ans+=l[len(l)-1]
    return ans



searchURL=baseURL1+query_split(kword)
l1=formAuthorList(br,searchURL)
l2=formURLList(br,searchURL)


l3=[]
for ele in l2:
    l5=visit_URL1(br,ele)
    l6=visit_URL2(br,ele)
    l7=visit_URL3(br,ele)
    l8=visit_URL4(br,ele)
    #l3.append(l4)


l4=list(zip(l1,l5,l6,l7,l8))
#print l1

df=pd.DataFrame(data=l4,columns=['Names','Publications','Co-Authors','Year of Publication','Journal'])
df.to_csv('output2.csv',index=False,header=True)
