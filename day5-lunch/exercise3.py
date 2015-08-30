#!/usr/bin/env python

filename="/Users/cmdb/qbb2015-homework/day5-lunch/results.out"
f=open(filename)

for line in f:
    if line.startswith(">"):
        ident=line.strip()
        count_alignment=0
        max_alignment=0
    elif line.lstrip().startswith("|"):
        alignment=line.strip()
        for locus in alignment:
            if locus=="|":
                count_alignment+=1
            else:
                if count_alignment>max_alignment:
                    max_alignment=count_alignment
                    count_alignment=0
                else:
                    count_alignment=0
        print ident,max_alignment
        
