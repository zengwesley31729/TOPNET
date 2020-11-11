#!/usr/bin/env python
# coding: utf-8

# In[2]:


import my_module_original as my
import networkx as nx
import numpy as np

#import packages
import os
from pandas import DataFrame
import re
import pandas as pd
#from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

dataname=re.compile(r'.+(?=\.)')
todo_list=[]
#input todo file folder path
to_do_dir =''
if os.path.exists(finish_dir):
    for file_name in os.listdir(to_do_dir):
        file_name_tmp=dataname.match(file_name)
        todo_list.append(file_name_tmp.group())

for i in todo_list:
            csv_path=os.path.join(to_do_dir,i)+'.csv'
            data = pd.read_csv(csv_path)
            G = nx.from_pandas_edgelist(data, source = "from_id", target="to_id")
            print("task:",i)
            print(i,nx.info(G))
            largest_cc = max(nx.connected_components(G), key=len)
            G2 = G.subgraph(list(largest_cc))
            influence=len(G2.nodes())/len(G.nodes())
            print("infulence rate:",i,influence)
            ave_path=nx.average_shortest_path_length(G2)
            print("average_shortest_path_length:",i,ave_path)
            global_efficiency=nx.global_efficiency(G2)/nx.global_efficiency(G)
            print("global_efficiency:",i,global_efficiency)
            print("task finished:",i)
            print("...")
            print("...")
            

            
