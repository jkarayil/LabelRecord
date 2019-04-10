
# coding: utf-8

# In[1]:

import pandas as pd
import os,re,sys
import numpy as np
import glob as glob


# In[2]:

def createNewDataFrame():
    
    columns = ['document_id','content','cat','subcat']
    df_ = pd.DataFrame(columns=columns)
    return(df_)


# In[3]:

def getcategories(foldername):
    cats = foldername.split('_')
    print("The cats are ", cats,len(cats))
    cat =''
    sub = ''     
    if (len(cats) == 1):
        cat = cats[0]
        sub = ''
    if (len(cats) == 2):
        cat = cats[0]
        sub = cats[1]
    if(len(cats) == 3):
        cat = cats[0]+'/'+cats[1]
        sub = cats[2]
    if(len(cats) == 4):
        cat = cats[0]+'/'+cats[1]
        sub = cats[2]+'/'+cats[3]
        
    return(cat,sub)    


# In[4]:

global df
df = createNewDataFrame()

clientFolder='/home/medilenz/OCR_Process/Firm_logic_july_03/'

paths = glob.glob(clientFolder+'*/')
for item in paths:
    pdffolders = glob.glob(item+'/*.pdf_work') 
    #print("THe item is ", item)
    cat,subcat = getcategories(item.split('/')[-2])
    for eachpdffolder in pdffolders:
        doc_id=eachpdffolder.split('/')[-1].split('.')[0]        
        textfile = glob.glob(eachpdffolder+'page_*[^_6].txt')                  
        if(len(textfile) < 2):
            with open(eachpdffolder+'/page_0001.txt', 'r') as myfile0:
                content = myfile0.read()                    
        else :
            with open(eachpdffolder+'/page_0001.txt', 'r') as myfile:
                content = myfile.read()
            with open(eachpdffolder+'/page_0002.txt', 'r') as myfile2:
                content = content + myfile2.read()
                 
        df = df.append([{'document_id':doc_id, 'content':content,'cat':cat, 'subcat': subcat}],ignore_index=True)                        


df.to_csv("../corpus/Full_corpus_fromClientFolder.csv")
