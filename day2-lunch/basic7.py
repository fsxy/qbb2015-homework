#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/day1/SRR072893.sam"
f=open(filename)

count=0

for i in f:
    fields=i.split()
    if fields[2]=="2L" and 10000<=int(fields[3])<=20000:
        count+=1
            
print "Number of reads that starts where you wanted:", count
            
     
