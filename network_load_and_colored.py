#!/usr/bin/env python
# coding: utf-8

import my_module_original as my
import networkx as nx
import numpy as np
import os
from pandas import DataFrame
import re
import pandas as pd
import matplotlib.pyplot as plt


#setting folder path
url_dir=''
finish_dir =''
to_do_dir =''

finish_list =[]
dataname=re.compile(r'.+(?=\.)')
pngname=re.compile(r'.+(?=\_rate)')
if os.path.exists(finish_dir):
    for file_name in os.listdir(finish_dir):
        file_name_tmp=pngname.match(file_name)
        finish_list.append(file_name_tmp.group())
        
todo_list=[]
if os.path.exists(finish_dir):
    for file_name in os.listdir(to_do_dir):
        file_name_tmp=dataname.match(file_name)
        todo_list.append(file_name_tmp.group())
        
todo_task=[]
for i in todo_list:
    if i not in finish_list:
        todo_task.append(i)
#print('finish_list:',finish_list)
#print('todo_list:',todo_list)
print('todo_task:',todo_task)
#scope_rate = open('scope_rate.txt', 'w')
if len(todo_task)==0:
    print('no new task system break')
    
else:
    
    for i in todo_task:
        keyword2=[]
        node_color=[]
        print("load url data from data_path")
        print("....")
        print("task:",i)
        #讀取id資料
        print("start load url data from file path")
        print("...")
        data_path = os.path.join(url_dir,i)+'.txt'
        print("load url data finished")
        print("...")
        #用正則表達示取出id
        print("start extract keyword")
        print("...")
        keyword=my.data_process(data_path)
        for key in keyword:
            if key not in keyword2:
                keyword2.append(key)
        #if len(keyword2)>200:
         #   print('data too big,do it alone')
          #  continue
        else:
            print("extract keyword finished")
            print("...")
            #讀入網路資料
            print("satrt read csv data")
            print("...")
            csv_path=os.path.join(to_do_dir,i)+'.csv'
            data = pd.read_csv(csv_path)
            #轉化成圖
            print("read csv data finished")
            print("...")
            print("start convert to network graph")
            print("...")
            print("It may take a while")
            print("...")
            G = nx.from_pandas_edgelist(data, source = "from_id", target="to_id")
            print("convert to network graph finished")
            #去重複id
            #不要用set去除重複,會有bug
            print("...")
            print("start keyword process")
            print("...")
            #keyword_unduplicate = keyword_color(keyword)
            #把有出現在keyword_unduplicate中的id標記成紅色
            print("keyword process finished")
            print("...")
            print("start make node color list")
            print("...")
            for j in G.nodes():
                if str(j) in keyword2:
                    node_color.append('red')
                else:
                    node_color.append('blue')
            print("make node color list finished")
            #清除先前的圖資料
            print("...")
            print("start output network image")
            print("...")
            plt.cla()
            #開一個20,20的畫板
            plt.figure(figsize=(20,20))
            #畫出有顏色的網路圖
            #紅色代表有出現在keyword中的id
            #藍色代表隱藏的朋友連結id
            #pos=nx.spring_layout(G)
            nx.draw_networkx(G, 
                            pos=nx.spring_layout(G),
                            node_color=node_color, 
                            edge_color="black", 
                            alpha=0.5,
                            style='solid',
                            with_labels=True)
            print("output network image finished")
            print("...")
            #輸出圖片
            print(" start save image")
            print("...")
            count=0
            for k in node_color:
                if k == 'red':
                    count+=1
            if len(keyword2)>0:
                
                tmp_rate= count/len(keyword2)
                rate = round(tmp_rate,2)
            else:rate=0
            output_path=os.path.join(finish_dir,i)+'_rate_'+str(rate)+'.png'
            plt.savefig(output_path)
        
            print("all task finished,great work")

