#!/usr/bin/env python

import pandas as pd

annotation="/Users/cmdb/qbb2015/rawdata/samples.csv"

samples=pd.read_csv(annotation, header=0)

samples.columns=["sample","sex","stage"]

for prefix in samples["sample"]:
    filename="/Users/cmdb/qbb2015/stringtie/"+prefix+"/t_data.ctab"
    df=pd.read_table(filename)
    df.columns=["t_id","chr","strand","start","end","tname","num_exons","length","gene_id","gene_name","cov","FPKM"]
    filter=df["tname"].str.contains("FBtr0331261")
    print df[filter]