#!/usr/bin/env python

import chrombits

data_format="/Users/cmdb/qbb2015-homework/day4/dm3.len"
data_source=["/Users/cmdb/qbb2015-homework/day4/DM3_Kc_BEAF.bed","/Users/cmdb/qbb2015-homework/day4/DM3_Kc_SuHW.bed"]

arr=chrombits.ChromosomeLocationBitArrays(fname=data_format)

beaf=arr.copy()
suhw=arr.copy()

beaf.set_bits_from_file(data_source[0])
suhw.set_bits_from_file(data_source[1])

a_and_not_b=beaf.union(suhw.complement())

print a_and_not_b.set_start_end_from_bits()