#!/usr/bin/env python

filename="/Users/cmdb/qbb2015-homework/day5-lunch/results.out"
f=open(filename)

for line in f:
    if line.startswith(">"):
        ident=line.strip()
    elif line.lstrip().startswith("Identities"):
        content=line.strip()
        print ident, content
