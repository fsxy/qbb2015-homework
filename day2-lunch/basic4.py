#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/day1/SRR072893.sam"
f=open(filename)

count=0
for i in f:
    fields=i.split()
    if "SRR" in fields[0]:
        count+=1
    if 1<=count<=10:
        print fields[2]
    elif count>10:
        break
        
