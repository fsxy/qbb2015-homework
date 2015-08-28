#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""

import sys

from fasta import FASTAReader

reader=FASTAReader(sys.stdin)

#while 1:
#    print reader.next()
    
for 1, (ident, seq) in enumerate(reader):      #because iterator protocol is defined in fasta.py
    print i, ident, seq