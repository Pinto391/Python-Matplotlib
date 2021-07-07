#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[11]:


company=['Google','Amazon','Apple','FB']
revenue=[90,135,89,55]
profit=[40,65,35,23]


# In[12]:


xpos=np.arange(len(company))
xpos


# In[19]:


plt.xticks(xpos,company)

plt.ylabel("Revenue(Billion)")
plt.xlabel('Company')
plt.title("US Tech Stocks")

plt.bar(xpos-.2,revenue, width=.4, label='Revenue')
plt.bar(xpos +0.2,profit, width=.4, label='profit')
plt.legend()


# In[ ]:




