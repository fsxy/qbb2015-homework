#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df=pd.read_table(annotation)

df.columns=["t_id","chr","strand","start","end","tname","num_exons","length","gene_id","gene_name","cov","FPKM"]

plotdf=df.sort("FPKM",ascending=False)

rows=plotdf.shape[0]
print rows
checkpoint1=int(rows/3)
checkpoint2=2*checkpoint1

plt.figure()
#plt.boxplot(plotdf["FPKM"][0:checkpoint1])
plt.boxplot(df["FPKM"][0:checkpoint1])
plt.title("Top 1 3rd of FPKM")
plt.savefig("FPKM_boxplot_3_1.png")

