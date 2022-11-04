#!/usr/bin/env python
# coding: utf-8

# In[199]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from collections import Counter



# In[200]:


nba = pd.read_csv('./Downloads/2018-19_pbp.csv', encoding='utf-8')
nba.sort_values(['GAME_ID'])


# In[201]:


def nba_funct1(GAME_ID):
    temp_nba = nba[nba['GAME_ID'] == GAME_ID]
    return temp_nba


# In[202]:


nba_funct1(21800022)


# In[203]:


nba_funct1(21800702)


# In[204]:


nba_funct1(21800958)


# In[205]:


nba_funct1(21800371)


# In[206]:


nba_funct1(21800419)


# In[207]:


def nba_funct2(GAME_ID):
    temp = nba[nba['GAME_ID'] == GAME_ID]
    player1 = Counter(temp['PLAYER1_NAME']).most_common()
    player2 = Counter(temp['PLAYER2_NAME']).most_common()
    player3 = Counter(temp['PLAYER3_NAME']).most_common()
    

    labels, ys = zip(*player1)
    xs = np.arange(len(labels)) 
    width = 1
    plt.figure(figsize=(45,12))
    plt.bar(xs, ys, width, align='center')
    plt.xticks(xs, labels)
    plt.yticks(ys)
     


# In[208]:


nba_funct2(21800025)


# In[209]:


nba_funct2(21800722)


# In[210]:


nba_funct2(21800200)


# In[211]:


nba_funct2(21800119)


# In[212]:


nba_funct2(21800416)


# In[213]:


def nba_funct3(GAME_ID):
    param_nba = nba.sort_values(['GAME_ID'])
    temp = param_nba[param_nba['GAME_ID'] == GAME_ID]
    x = (temp.value_counts(["PLAYER1_NAME", "PLAYER2_NAME"])>1)
    return x


# In[214]:


nba_funct3(21800027)


# In[215]:


nba_funct3(21800716)


# In[216]:


nba_funct3(21800005)


# In[217]:


nba_funct3(21801067)


# In[218]:


nba_funct3(21801001)


# In[ ]:




