#!/usr/bin/env python

filename="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

#f=open(filename)

#for line in f:
#    fields=line.split()       #fields is now a list. if printed, it looks like this : ['abc' 'ddd' 'dds' 'sfe'] 
#    if "tRNA" in fields[9]:
#        print line,          #the comma stops adding an extra new line by print. because we already have a new line in the original file.
        
#f.close()

#f=open(filename)

#for line_count, line in enumerate(f):        
#    if line_count<=10:
#        pass
#    elif line_count<=15:
#        print line,
#    else:
#        break
    
f=open(filename)
name_counts={}
    
for line_count, data in enumerate(f):
    fields=data.split()
    gene_name=fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name]=1
    else:
        name_counts[gene_name]+=1
        
#Iterate key, value pairs from the name counts dictionary
for key,value in name_counts.iteritems():
    print key, value