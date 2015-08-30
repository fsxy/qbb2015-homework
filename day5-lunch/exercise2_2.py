#!/usr/bin/env python

import matplotlib.pyplot as plt

f=open("/Users/cmdb/qbb2015-homework/day5-lunch/exercise2_intermediate")
plot_data={"score":[],"evalue":[]}
for line in f:
    fields=line.rstrip("\n").split(" ")
    if len(fields) !=11:
        continue
    plot_data["score"].append(float(fields[4]))      #Don't forget to float it otherwise strang error will be thrown.
    plot_data["evalue"].append(float(fields[10]))
    
plt.figure()
plt.hist(plot_data["score"])
plt.savefig("histo_score.png")

plt.figure()
plt.hist(plot_data["evalue"])
plt.savefig("histo_evalue.png")

plt.figure()
plt.scatter(plot_data["score"],plot_data["evalue"])
plt.savefig("scatterplot.png")