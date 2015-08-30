#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df=pd.read_table(annotation)

df.columns=["t_id","chr","strand","start","end","tname","num_exons","length","gene_id","gene_name","cov","FPKM"]

plotdf=df.sort("FPKM",ascending=False).reset_index()
filter_zero=plotdf["FPKM"]>0
plotdf_no_zero=plotdf[filter_zero]


rows=plotdf_no_zero.shape[0]

checkpoint1=int(rows/3)
checkpoint2=2*checkpoint1
#print plotdf_no_zero["FPKM"]
#print plotdf_no_zero
plt.figure()
plt.boxplot([plotdf_no_zero["FPKM"][:checkpoint1],plotdf_no_zero["FPKM"][checkpoint1:checkpoint2],plotdf_no_zero["FPKM"][checkpoint2:]])

plt.title("Boxplot of PKM")
plt.savefig("FPKM_boxplot.png")

