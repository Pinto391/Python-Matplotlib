#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


blood_suger= [113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_suger, bins=[80,100,125,150], rwidth=0.95)


# In[11]:


blood_sugerd_men=[113,85,90,150,149,88,93,115,135,80,77,82,129]
blood_suger_women=[67,98,89,120,133,150,84,69,89,79,120,112,100]

plt.xlabel('Suger Range')
plt.ylabel('Total o of patients')
plt.title('Blood Suger Analysis')
plt.hist([blood_sugerd_men,blood_suger_women], bins=[80,100,125,150], rwidth=0.95, color=['green','red'],label=['Men','Women'])
plt.legend()


# In[ ]:




