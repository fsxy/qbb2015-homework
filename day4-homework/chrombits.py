from __future__ import division       #so that "/" followed by integers will give float result instead of integer.

import numpy
import copy

class ChromosomeLocationBitArrays(object):
    
    def __init__(self, dicts=None, fname=None):
        #If dict  provided, use fname to initialize. Otherwise use fname to initialize.
        if dicts is not None:
            arrays=dicts
        else:
            arrays={}
        
        if fname is not None:
        
            for line in open(fname):
                fields=line.split()
                name=fields[0]
                size=int(fields[1])
                arrays[name]=numpy.zeros(size, dtype=bool)
        self.arrays=arrays
            
    def set_bits_from_file(self,fname):
        for line in open(fname):
            fields=line.split()
            chrom=fields[0]
            start=int(fields[1])
            end=int(fields[2])
            self.arrays[chrom][start:end]=1           #the "1" will be automatically expanded to match the size of the array.

    def intersect(self,other):
        rval={}
        for chrom in self.arrays:    #this means chrom in the keys of arrays1.
            rval[chrom]=self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
        
    def copy(self):
        return ChromosomeLocationBitArrays(dicts=copy.deepcopy(self.arrays))
    
    def union(self,other):
        rval={}
        for chrom in self.arrays:    #this means chrom in the keys of arrays1.
            rval[chrom]=self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
    
    def complement(self):
        rval={}
        for chrom in self.arrays:    #this means chrom in the keys of arrays1.
            rval[chrom]= ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
        
        
    def set_start_end_from_bits(self):
        output=[]
        for chrom in self.arrays:
            start=0
            end=0
            previous_status=False
            for index, locus in enumerate(self.arrays[chrom]):
                if locus==True:
                    if previous_status==False:
                        start=index
                        previous_status=True
                    else:
                        pass
                elif previous_status==True:
                    end=index
                    previous_status=False
                    output.append((chrom,start,end))
                else:
                    pass
            print "1 small loop complete"
        return output
                