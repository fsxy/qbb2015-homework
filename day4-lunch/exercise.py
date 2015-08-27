#!/usr/bin/env python


from __future__ import division       #so that "/" followed by integers will give float result instead of integer.
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import copy     #used for copying dictionary
import numpy

data_source=["/Users/cmdb/qbb2015-homework/day4/DM3_Kc_BEAF.bed","/Users/cmdb/qbb2015-homework/day4/DM3_Kc_SuHW.bed","/Users/cmdb/qbb2015-homework/day4/DM3_Kc_CTCF.bed"]


def arrays_from_len_file(fname):
    arrays={}               #this is a dictionary whose key is the name of chromosome and value is an array that contains the number of zeros equal to the length of the corresponding chromosome.
    for line in open(fname):
        fields=line.split()
        name=fields[0]
        size=int(fields[1])
        arrays[name]=numpy.zeros(size,dtype=bool)      #the numpy.zeros() creates an array whose length equals the length of the corresponding chromosome.
    return arrays
    
    
    
def set_bits_from_file(arrays,fname):
    for line in open(fname):
        fields=line.split()
        chrom=fields[0]
        start=int(fields[1])
        end=int(fields[2])
        arrays[chrom][start:end]=1           #the "1" will be automatically expanded to match the size of the array.
    
arrays=arrays_from_len_file("/Users/cmdb/qbb2015-homework/day4/dm3.len")    

arrays_beaf=copy.deepcopy(arrays)
arrays_suhw=copy.deepcopy(arrays)
arrays_ctcf=copy.deepcopy(arrays)

print "arrays_beaf",arrays_beaf["chr2L"][2:10]

set_bits_from_file(arrays_beaf,data_source[0])
set_bits_from_file(arrays_suhw,data_source[1])
set_bits_from_file(arrays_ctcf,data_source[2])

previous_status=""
status_count={}

print "begin loop"

for chromo in arrays.keys():
    print "chromosome:",chromo,
    for locus_index,locus in enumerate(arrays[chromo]):
        status=str(arrays_beaf[chromo][locus_index])+str(arrays_suhw[chromo][locus_index])+str(arrays_ctcf[chromo][locus_index])
        #print "locus_index:",locus_index
        #print "locus:",locus
        #print "status:",status
        
        if previous_status==status:
            pass
        elif status not in status_count.keys():
            status_count[status]=1
            previous_status=status
        else:
            status_count[status]+=1
            previous_status=status
            
        
    print "1 big loop complete"
    print status_count
            
            
total_1=status_count["FalseFalseTrue"]+status_count["FalseTrueFalse"]+status_count["TrueFalseFalse"]
total_2=status_count["FalseTrueTrue"]+status_count["TrueFalseTrue"]+status_count["TrueTrueFalse"]
total_3=status_count["TrueTrueTrue"]

        
print "Number of regions bound by only 1 protein: %d" % total_1
print "Number of regions bound by only 2 protein: %d" % total_2
print "Number of regions bound by 3 protein: %d" % total_3

print "Abc:",status_count["TrueFalseFalse"]
print "aBc:",status_count["FalseTrueFalse"]
print "ABc:",status_count["TrueTrueFalse"]
print "abC:",status_count["FalseFalseTrue"]
print "AbC:",status_count["TrueFalseTrue"]
print "aBC:",status_count["FalseTrueTrue"]
print "ABC:",status_count["TrueTrueTrue"]

plt.figure()
venn3((status_count["TrueFalseFalse"],status_count["FalseTrueFalse"],status_count["TrueTrueFalse"],status_count["FalseFalseTrue"],status_count["TrueFalseTrue"],status_count["FalseTrueTrue"],status_count["TrueTrueTrue"]),set_labels=('BEAF','SuHW','CTCF'))
plt.savefig("venn")


#for key, value in arrays.iteritems():       #dictionary.iteritems() returns a tuple containing iterating key value pair
#    print key,type(value),value.shape,numpy.sum(value)

#grep "^chr2R" DM3_Kc_DNase.bed | ./intersect.py  dm3.len DM3_phastCons.bed  /dev/stdin       this can select only the chromosome 2R result. compared to this command:
#./intersect.py dm3.len DM3_phastCons.bed DM3_Kc_DNase.bed 
#the "/dev/stdin" is meant to force the python script to get the input from pipeline because originally the python script doesn't take input from stdin and /dev/stdin makes standard input look like a file for python script.