#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns


# In[4]:


import matplotlib.pyplot as plt


# In[7]:


dataset = pd.read_csv("C:\\Users\\Hp\\Downloads\\New_Sample - Copy.csv")
dataset


# In[8]:


dataset.isnull().sum()


# In[9]:


dataset.info()


# In[16]:


sns.heatmap(dataset.corr(), annot=True)


# In[17]:


plt.figure(figsize=(10,100))
sns.countplot(x="Name", data=dataset, hue='MRP')


# In[25]:


plt.figure(figsize=(200,200))
sns.countplot(y='Best Price',data=dataset)
plt.ylabel('Name')
plt.show()


# In[26]:


sns.pairplot(dataset)


# In[27]:


plt.xlabel('Name')
plt.ylabel('Type of sell')
plt.scatter(dataset['Name'],dataset['Type of Sell'])


# In[28]:


dataset.hist()


# In[34]:


dataset.pop("Type of Sell")


# In[36]:


dataset.pop("Category")


# In[37]:


dataset.corr()


# In[40]:


cat_cols = list(dataset.columns)
cat_cols.remove('Best Price')
cat_cols.remove('Name')
fig,axarr = plt.subplots(nrows=len(cat_cols),figsize=(12,30))
for i in range(len(cat_cols)):
    sns.countplot(x=cat_cols[i],ax=axarr[i],data=dataset)
plt.tight_layout();


# In[ ]:




