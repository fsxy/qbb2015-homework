#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/day1/SRR072893.sam"
f=open(filename)

count=0
for i in f:
    if "NM:i:0" in i:
        count+=1
        
print "Number of perfect hits:", count