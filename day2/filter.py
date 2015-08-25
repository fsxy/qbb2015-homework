#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f=open(filename)

for line in f:
    fields=line.split()       #fields is now a list. if printed, it looks like this : ['abc' 'ddd' 'dds' 'sfe'] 
    if "tRNA" in fields[9]:
        print line,          #the comma stops adding an extra new line by print. because we already have a new line in the original file.