#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation,comment='#',header=None)

df.columns=["chromosomes","database","type","start","end","score","strand","frame","attributes"]

filter=df["attributes"].str.contains("Sxl")
plt.figure()
plt.plot(df[filter]["start"])
plt.xlabel("gene")
plt.ylabel("start position")
plt.title("Sxl")
plt.savefig("SxlStarts.png")