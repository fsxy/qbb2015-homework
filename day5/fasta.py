#!/usr/bin/env python



class FASTAReader(object):
    def __init__(self, file):
        self.file=file
        self.last_ident=None   # to store the previous header
        
    def next(self):             #Iterator protocol, together with the function __iter__()
        if self.last_ident is None:            
            line = self.file.readline()            #call this script by "cat ./subset.fa | ./parse_single.py"
            assert line.startswith(">"), "Not valid fasta"
            ident= line[1:].rstrip("\r\n")    #remove all \r and \n on the right end of the string and return this modified string.
        else:
            ident=self.last_ident
            
        sequences=[]
        while True:
            line = self.file.readline()
            if not line:
                break
            if line.startswith(">"):
                self.last_ident= line[1:].rstrip("\r\n")
                break
            else:
                sequences.append(line.strip())
                
        if len(sequences)==0:
            raise StopIteration

        sequence="".join(sequences)      #join() takes a list of strings and catenates them using things inside the "" as delimiter.

        return ident, sequence
        
    def __iter__(self):            #Iterator protocol, together with the function next(). Everytime an object of this class is asked to be iterated (e.g. being in an enumerate()), it will call the function next() time by time.
        return self
