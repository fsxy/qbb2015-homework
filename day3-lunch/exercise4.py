#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as nu

def log2(x):
    return nu.log(x)/nu.log(2)

expression1="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
expression2="/Users/cmdb/qbb2015/stringtie/SRR072905/t_data.ctab"

df1=pd.read_table(expression1)
df2=pd.read_table(expression2)

R_value=df1["FPKM"]
G_value=df2["FPKM"]

M_value=log2(R_value/G_value)
A_value=0.5*log2(R_value*G_value)

plt.figure()
plt.scatter(A_value,M_value)
plt.savefig("maplot.png")

#df.columns=["t_id","chr","strand","start","end","tname","num_exons","length","gene_id","gene_name","cov","FPKM"]

#filter_zero=df["FPKM"]>0
#plotdf_no_zero=df[filter_zero]

#rows=plotdf_no_zero.shape[0]

#plotdf_no_zero=plotdf_no_zero.reset_index()



