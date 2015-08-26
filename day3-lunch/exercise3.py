#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as nu
from scipy.stats import gaussian_kde

annotation="/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df=pd.read_table(annotation)

#df.columns=["t_id","chr","strand","start","end","tname","num_exons","length","gene_id","gene_name","cov","FPKM"]

filter_zero=df["FPKM"]>0
plotdf_no_zero=df[filter_zero]

rows=plotdf_no_zero.shape[0]

plotdf_no_zero=plotdf_no_zero.reset_index()

density=gaussian_kde(plotdf_no_zero["FPKM"])
xs=nu.linspace(0,rows,2000)
density.covariance_factor=lambda : .25
density._compute_covariance()

plt.figure()
plt.plot(xs,density(xs))
#plt.boxplot(df["FPKM"][0:checkpoint1])
plt.title("Density plot")
plt.savefig("density_plot.png")

