#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np
import glob
import os
  
# merging the files
joined_files = os.path.join("database", "JC-201*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df_one = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df_one


# In[2]:


# merging the files
joined_files = os.path.join("database", "JC-2020*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df_two = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df_two


# In[3]:


result = pd.concat([df_one, df_two])
result


# In[4]:


result.to_csv('database/citibike.csv', index=False)


# In[5]:


# merging the files
joined_files = os.path.join("database", "JC-2022*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df_fr = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df_fr


# In[6]:


# merging the files
joined_files = os.path.join("database", "JC-2023*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df_fv = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df_fv


# In[7]:


result2 = pd.concat([ df_fr,df_fv])

result2


# In[8]:


result2.to_csv('database/citibike_new.csv', index=False)


# In[ ]:




