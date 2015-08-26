#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation,comment='#',header=None)

df.columns=["chromosomes","database","type","start","end","score","strand","frame","attributes"]

filter1=df["attributes"].str.contains("Sxl")
df2=df[filter1]
filter2=df2["type"].str.contains("transcript")

plt.figure()
plt.plot(df2[filter2]["start"])
plt.xlabel("gene")
plt.ylabel("start position")
plt.title("Sxl-transcript")
plt.savefig("Sxl-transcriptStarts.png")