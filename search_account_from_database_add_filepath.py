#!/usr/bin/env python
# coding: utf-8
import numpy as np
import os
from pandas import DataFrame
import re
import pandas as pd

###folder path setting
#放入完成搜尋後output資料夾路徑
finish_dir = ''
#放入帳號資料庫路徑
search_path = ''
#放入批次待查找ID的URL資料夾路徑
to_do_dir =''
#放入要output csv檔案路徑
output_dir=''



# def  function 
# coding = utf-8

#id_finder
##use regular expression to find id in url

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

###search id in database

keyword = []
 
#defined keyword don't search
exclude_word = []
 
#defined document type for search
file_name_list = ['.csv']
 
#defined file name don't search
exclude_file_name_list = ['all']

#defined a search function to iterate search keyword inside document in folder
results=[]
filepath=[]
def search(search_path):

 #check path exist
    if os.path.exists(search_path):
    #獲取search_name目录下的文件/文件夹名，并遍历文件
        #time =0
        for file_name in os.listdir(search_path):
            
            full_path = os.path.join(search_path,file_name)
            #flag 文件名是否包含file_name_list，不包含exclude_file_name_list
            flag = False
             #flag_path 第一次打印文件名
            flag_filepath = True
            i = 0
             #check is it a document
            ####use full_path，not file_name,
            if os.path.isfile(full_path):
               #check document  name and type incould the type defined in file_name_list
                for extend in file_name_list:
                    if extend in file_name:
                        flag = True
                        #判断文件名中是否不包含exclude_file_name_list中的文件名
                       # for exclude in exclude_file_name_list:
                        #    if exclude in file_name:
                         #       flag = False
                #if flag = true , search the document contnet by line
                if flag:
                    
                    flag = False
                    ff = open(full_path,'r',encoding="utf-8")
                    for line in ff:
                        i+=1
                        FLAG = False
                        if len(exclude_word)==0:
                            for KEY in keyword:
                                if KEY in line:
                                    FLAG = True
                                    break
                        else:
                            for KEY in keyword:
                                if KEY in line:
                                    FLAG = True
                                    break
                            #for UKEY in exclude_word:
                             #   if UKEY in line:
                              #      FLAG = False
                               #     break           
                        if FLAG:
                            FLAG = False
                            
                            #print document path
                            #if flag_filepath:
                            #print("file path: "+full_path)
                            filepath.append(full_path)
                                #flag_filepath = False
                            #print("line %d" %i)
                            #print(line)
                            results.append(line)
            #if it is a folder,use search function for iterate
            if os.path.isdir(full_path):
                search(full_path)
    return [results,filepath]
    #return filepath



###function for account:

#1.account_result_spilt
def result_spilt(res):
    k=[]
    for a in res:
        a=str(a)
        spilt_result=a.split('\t')
        k.append(spilt_result)
    return k

#2.score
#change input name as data
#function for path_result
#path_spilt
def path_spilt(path):
    pathspilt=[]
    for a in path:
        #str=a
        spilt_result=a.split('/')
        spilt_result=spilt_result[6]
        pathspilt.append(spilt_result)
    return pathspilt



finish_list =[]

dataname=re.compile(r'.+(?=\.)')
if os.path.exists(finish_dir):
    for file_name in os.listdir(finish_dir):
        file_name_tmp=dataname.match(file_name)
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


if len(todo_task)==0:
    print('no new task system break')
    
else:
    results=[]
    filepath=[]
    for todo in todo_task:
        print("load url data from data_path")
        print("....")
        print("task:",todo)
        data_path = os.path.join(to_do_dir,todo)+'.txt'
        print("exteact keyword")
        tmp=data_process(data_path)
        #search keyword
        keyword = tmp
        #use search function
        print("....")
        print("search keyword from database")
        print("....")
        print("it may take a while ....")
        results,filepath=search(search_path)
        print(filepath)
        #res =results
        print("....")
        print("result process")
        spilt=result_spilt(results)
        path=path_spilt(filepath)
        print("....")
        print("convert to dataframe")
        results_account=pd.DataFrame(spilt,columns = ['from_id', 'form_name', 'to_id', 'to_name'])
        results_account['file_path']=path
        #results_account
        #print(path)
        print("....")
        print("output csv file:")
        
        output_path = os.path.join(output_dir,todo)+'.csv'
        print(output_path)
        results_account.to_csv(output_path, index = False, header=True)
        print("....")
        print("finish")
        print("....")
        results=[]
        filepath=[]





