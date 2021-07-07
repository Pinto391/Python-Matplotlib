#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


exp_vlas=[1400,600,300,410,250]
exp_label=['Home Rent','Food','Phone/Internet Bill','Car','Others Utilities']


# In[27]:


plt.pie(exp_vlas,labels=exp_label,radius=1.5,autopct='%0.1f%%',shadow=True,
       explode=[0,0,0,0.2,0.2],startangle=45)
plt.show()
plt.savefig("Piechart.png",bbox_inches="tight",pad_inches=2,transparent=True)


# In[23]:





# In[ ]:




