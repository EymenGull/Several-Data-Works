#!/usr/bin/env python
# coding: utf-8

# In[2]:
#link of the data : https://data.ibb.gov.tr/dataset/hourly-public-transport-data-set
#aim of this work : Calculating the total hourly uses of different modes of transports for January 2021 and May 2021.
#                   Calculating the total hourly uses of different transfer types (AKTARMA, NORMAL) for June 2020 and in September 2020.
#                   Calculating the daily totals of passenger numbers and passage numbers for August 2020.

import pandas as pd
import numpy as np
import sys

from matplotlib import pyplot as plt
from scipy import stats


def ibbfunc(address, valofcol):
    datas = pd.read_csv(address)
    datas['DATE_TIME'] = pd.DatetimeIndex(datas['DATE_TIME']).hour
    hourly_list = datas.groupby(['DATE_TIME',valofcol])['NUMBER_OF_PASSENGER'].sum()
    cleaner = hourly_list.index.to_frame()
    cleaner['NOP'] = hourly_list
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ): display(cleaner)
    print(cleaner.shape)
    cleaner.plot(figsize = (18,6),x='DATE_TIME',y='NOP')
    return(cleaner)



# In[23]:


ibbfunc('./Downloads/hourly_transportation_202101.csv', 'TRANSFER_TYPE')


# In[24]:


ibbfunc('./Downloads/hourly_transportation_202105.csv', 'TRANSPORT_TYPE_DESC')


# In[34]:


data20 = pd.read_csv('./Downloads/hourly_transportation_202004.csv')
data20['DATE_TIME'] = pd.DatetimeIndex(data20['DATE_TIME']).day
daily_list = data20.groupby(['DATE_TIME','LINE'])['NUMBER_OF_PASSENGER'].sum()
daily_list.sort_values(ascending=False)
cleaner = daily_list.index.to_frame()
cleaner['NOP'] = daily_list

display(cleaner)
print(cleaner.shape)
with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ): display(cleaner)
#AKSARAY-HAVALİMANI is the busiest line in all days


# In[54]:


data20 = pd.read_csv('./Downloads/hourly_transportation_202008.csv')
data20['DATE_TIME'] = pd.DatetimeIndex(data20['DATE_TIME']).day
daily_list = data20.groupby(['DATE_TIME','LINE'])['NUMBER_OF_PASSENGER'].sum()
daily_list.sort_values(ascending=False)
cleaner = daily_list.index.to_frame()
cleaner['NOP'] = daily_list
with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ): display(cleaner)
print(cleaner.shape)

passenger_np = np.zeros((614,1))
passage_np = np.zeros((1,614))

data20_pass = pd.read_csv('./Downloads/hourly_transportation_202008.csv')
data20_pass['DATE_TIME'] = pd.DatetimeIndex(data20_pass['DATE_TIME']).day
daily_list = data20_pass.groupby(['DATE_TIME','LINE'])['NUMBER_OF_PASSAGE'].sum()
daily_list.sort_values(ascending=False)
cleanerP = daily_list.index.to_frame()
cleanerP['NOP'] = daily_list
with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.precision', 3,
                           ): display(cleanerP)
print(cleanerP.shape)




# In[ ]:




