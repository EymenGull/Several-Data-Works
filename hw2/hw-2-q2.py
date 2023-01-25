#!/usr/bin/env python
# coding: utf-8

# In[170]:

#aim of the project  : Constructing a complete list of all artists appearing in the dictionary.
#                      Then using Counter function count how many times each artist appears.
#                      Filtering out those artists that appear fewer than 100 times, and then sorting the remaining from the most popular to least popular.


from urllib.request import urlopen

import  matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from collections import Counter
import pandas as pd
import json
import yaml

import numpy as np


# In[171]:


with urlopen('https://raw.githubusercontent.com/arch-raven/spotify-recsys/main/spotify_million_playlist/dataset/data/mpd.slice.0-999.json') as file:
    spotify = json.load(file)

artist=[]
songs=[]
spotify


# In[172]:


playlist_n =spotify['playlists']
play_ = playlist_n[0]['tracks']
artists = play_[0]['artist_name']
artists


# In[173]:


len(list_)


# In[174]:


for i in playlist_n:
    list_ = i['tracks']
    for j in list_:
        artist.append(j['artist_name'])

artist


# In[175]:


counted = Counter(artist).most_common()


# In[176]:


l_counted = counted[:96]


# In[177]:


l_counted


# In[178]:


labels, ys = zip(*l_counted)
xs = np.arange(len(labels)) 
width = 1
plt.figure(figsize=(100,15))
plt.bar(xs, ys, width, align='center')
plt.xticks(xs, labels)
plt.yticks(ys)


# In[179]:


for i in playlist_n:
    list_ = i['tracks']
    for j in list_:
        songs.append(j['track_name'])

songs


# In[180]:


counted = Counter(songs).most_common()


# In[181]:


counted


# In[194]:


l_counted = counted[:110]


# In[195]:


l_counted


# In[196]:


labels, ys = zip(*l_counted)
xs = np.arange(len(labels)) 
width = 1
plt.figure(figsize=(100,15))
plt.bar(xs, ys, width, align='center')
plt.xticks(xs, labels)
plt.yticks(ys)


# In[ ]:




