#!/usr/bin/env python

import pandas as pd

annotation="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation,comment='#',header=None)

#print df.head(5)

#print df.describe()

#print df.info()

#print df[1:5]      #print line 1,2,3,4  (without line 0 and line 5)

df.columns=["chromosomes","database","type","start","end","score","strand","frame","attributes"]
#df.info()

#print df.sort("type", ascending=False)

#Subset "chromosomes","start", and "end" columns

#print df[["chromosomes","start","end"]][9:15]        #the order of the two "[]" doesn't matter here.

#print df.shape

#df2=df["start"]

#df2.to_csv("startColumn.txt",sep='\t',index=False)



#Get a list of boolean that specifies the feature of rows.
filter=df["start"]<10

print filter
print df[filter]
print filter.shape
print df[filter].shape
print df[~filter]   #print those false instead of those true