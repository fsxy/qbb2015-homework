#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata=pd.read_csv("~/qbb2015/rawdata/samples.csv")
metadata2=pd.read_csv("~/qbb2015/rawdata/replicates.csv")

Sxl_female=[]
Sxl_male=[]
Sxl_female_replicate=[0,0,0,0]
Sxl_male_replicate=[0,0,0,0]

for sample_female in metadata[metadata["sex"]=="female"]["sample"]:
    dfdf_female=pd.read_table("~/qbb2015/stringtie/"+sample_female+"/t_data.ctab")
    filter_female=dfdf_female["t_name"].str.contains("FBtr0331261")
    Sxl_female.append(dfdf_female[filter_female]["FPKM"].values)
    
for sample_male in metadata[metadata["sex"]=="male"]["sample"]:
    dfdf_male=pd.read_table("~/qbb2015/stringtie/"+sample_male+"/t_data.ctab")
    filter_male=dfdf_male["t_name"].str.contains("FBtr0331261")
    Sxl_male.append(dfdf_male[filter_male]["FPKM"].values)
    
for sample_female_replicate in metadata2[metadata2["sex"]=="female"]["sample"]:
    dfdf_female_replicate=pd.read_table("~/qbb2015/stringtie/"+sample_female_replicate+"/t_data.ctab")
    filter_female_replicate=dfdf_female_replicate["t_name"].str.contains("FBtr0331261")
    Sxl_female_replicate.append(dfdf_female_replicate[filter_female_replicate]["FPKM"].values)
    
for sample_male_replicate in metadata2[metadata2["sex"]=="male"]["sample"]:
    dfdf_male_replicate=pd.read_table("~/qbb2015/stringtie/"+sample_male_replicate+"/t_data.ctab")
    filter_male_replicate=dfdf_male_replicate["t_name"].str.contains("FBtr0331261")
    Sxl_male_replicate.append(dfdf_male_replicate[filter_male_replicate]["FPKM"].values)
    


plt.figure()
line1, =plt.plot(Sxl_female)
line2, =plt.plot(Sxl_male)
line3, =plt.plot(Sxl_female_replicate,'o')
line4, =plt.plot(Sxl_male_replicate,'o')

plt.legend((line1,line2,line3,line4),('female','male','female_replicate','male_replicate'),loc='best',bbox_to_anchor=(1.05,1),borderaxespad=0.)

plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.xticks(range(len(Sxl_female)),["10","11","12","13","14A","14B","14C","14D"])
plt.yticks(range(0,350,50))
plt.title("Timecourse of Sxl")
plt.savefig("timecourse.png")


