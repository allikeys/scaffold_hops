import numpy
from pandas import DataFrame
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

##Untested!!##

df = DataFrame.from_csv("../Results/seqAlignMatrix.csv")
df = df.truncate(before="12S_PROFR", after="4CL2_TOBAC") #To make it run faster for testing 
df = df.truncate(before="12S_PROFR", after="4CL2_TOBAC", axis="columns") #To make it run faster 
print(df)
G = nx.from_pandas_adjacency(df)
print(nx.info(G))
pos = nx.kamada_kawai_layout(G) #To arrange graph more clearly <- Other options for this
nx.draw(G, pos, with_labels=True)
plt.show()