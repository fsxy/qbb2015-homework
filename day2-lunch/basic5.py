#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/day1/SRR072893.sam"
f=open(filename)

chromosomes={"2L":0,"2R":0,"3L":0,"3R":0,"4":0,"X":0}

for i in f:
    fields=i.split()
    for chrome in chromosomes:
        if fields[2]==chrome:
            chromosomes[chrome]+=1
            
for key, value in chromosomes.iteritems():
    print key, value
            
     
