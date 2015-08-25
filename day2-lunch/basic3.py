#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/day1/SRR072893.sam"
f=open(filename)

count=0
for i in f:
    if "NH:i:1" in i:
        count+=1
        
print "Number of reads that map to one location:", count