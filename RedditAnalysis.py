import bz2
import json
import pandas as pd
import numpy as np
import os
import nltk
from nltk.corpus import stopwords

bz_file=bz2.BZ2File("RC_2015-01.bz2")

id1=[]
l=[]
keys=[]
values=[]
c=0
for line in bz_file:
	if c>100:
		break
	else:
		l.append(line)
		c+=1 

for i in range(0,len(l)):
	l[i]=l[i].replace("{","")
	l[i]=l[i].replace("}","")
	l[i]=l[i].split(",")
	for j in range(len(l[i])):
		l[i][j]=l[i][j].split(":")

for i in range(0,len(l)):
	for j in range(0,len(l[i])):
		if len(l[i][j])==2:
			keys.append(l[i][j][0])
			values.append(l[i][j][1])
		elif len(l[i])==1:
			keys.append(l[i][j][0])
			values.append('0')

print keys,values
print len(keys),len(values)
total=zip(keys,values)

df=pd.DataFrame(data=total)
df.to_csv("Reddit.csv")