#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import networkx as nx
import numpy as np
#import chart_studio.plotly as py
#import plotly.graph_objs as go
#import glob
#import networkx.algorithms.community as nxcom

#get_ipython().run_line_magic('matplotlib', 'notebook')

#import packages
import os
from pandas import DataFrame
import re
import pandas as pd
#from matplotlib.font_manager import FontProperties
#import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
#import matplotlib.ticker as mtick


# In[3]:


# def  function 
# coding = utf-8

#id_finder
data_path=''
def data_process(data_path):
    #load data
    data=open(data_path)
    data=str(data.readlines())
    #defined regular expression
    pattern = re.compile(r'(?<=id=)\d+\.?\d*')
    #use regular expression to find id in url
    pattern_find_id = pattern.findall(data)
    
    return pattern_find_id



#function for account:
1.#account_result_spilt
def result_spilt(res):
    k=[]
    for a in res:
        #str=a
        spilt_result=a.split('\t')
        k.append(spilt_result)
    return k

#2.score
#change input name as data
def sum_score(data):
    data=pd.DataFrame(data)
    data_sum = list(map(lambda x:float(x), data[1]))
    sum_result=sum(data_sum)
    return sum_result

#function for path_result
#path_spilt
def path_spilt(path):
    pathspilt=[]
    for a in path:
        #str=a
        spilt_result=a.split('_')
        spilt_result=spilt_result[2]
        pathspilt.append(spilt_result)
    return pathspilt

#group and sort
#change input name as path
def group_sort(path):
    #load data
    data_list = pd.DataFrame({'data': path})
    data_group = data_list.groupby('data')
    data_count = pd.DataFrame({'data_group_count': data_group.size()})
    #sort by count
    data_group_count_sorted = data_count.sort_values(by='data_group_count', ascending=False)
    data_group_count_sorted = pd.DataFrame(data_group_count_sorted)
    return data_group_count_sorted
