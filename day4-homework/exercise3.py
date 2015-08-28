#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import chrombits

data_format="/Users/cmdb/qbb2015-homework/day4/dm3.len"
data_source=["/Users/cmdb/qbb2015-homework/day4/DM3_Kc_BEAF.bed","/Users/cmdb/qbb2015-homework/day4/DM3_Kc_SuHW.bed","/Users/cmdb/qbb2015-homework/day4/DM3_Kc_CTCF.bed"]

arr=chrombits.ChromosomeLocationBitArrays(fname=data_format)

beaf=arr.copy()
suhw=arr.copy()
ctcf=arr.copy()


beaf.set_bits_from_file(data_source[0])
suhw.set_bits_from_file(data_source[1])
ctcf.set_bits_from_file(data_source[2])

union_object=beaf.union(suhw.union(ctcf))

union_bed_like=union_object.set_start_end_from_bits()

count_bind={}

for region in union_bed_like:    #region is a tuple
    
    chrom=region[0]
    start=int(region[1])
    end=int(region[2])
    
    if any(beaf.arrays[chrom][start:end]):
        status_locus="A"
    else:
        status_locus="a"
        
    if any(suhw.arrays[chrom][start:end]):
        status_locus=status_locus+"B"
    else:
        status_locus=status_locus+"b"
        
    if any(ctcf.arrays[chrom][start:end]):
        status_locus=status_locus+"C"
    else:
        status_locus=status_locus+"c"
        
    if status_locus not in count_bind.keys():
        count_bind[status_locus]=1
    else:
        count_bind[status_locus]+=1
            
venn_list=[count_bind["Abc"],count_bind["aBc"],count_bind["ABc"],count_bind["abC"],count_bind["AbC"],count_bind["aBC"],count_bind["ABC"]]

plt.figure()
venn3(venn_list,set_labels=('BEAF','SuHW','CTCF'))
plt.savefig("venn_comparison_union")