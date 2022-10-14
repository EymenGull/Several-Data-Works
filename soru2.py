#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np 
import pandas as pd
import sys

from matplotlib import pyplot as plt
from scipy import stats

data = pd.read_csv('./Desktop/fish_stableIsotopes_beaufort_stanek.csv')
data


# In[16]:


meanL = data.groupby(['Location','mmLength'])['mmLength'].mean()
cleaner = cleaner = meanL.index.to_frame()
cleaner


# In[27]:


data['Date'] = pd.DatetimeIndex(data['Date']).year
stat_diff = pd.crosstab(data['Date'],data['mmLength'])
stat_diff

#couldn't be aware of if there is a difference or not because the list is too long to decide. 


# In[32]:


#I couldn't finish the second question because I spent too much time on the first question. I'm embarrassed about this.


# In[ ]:




