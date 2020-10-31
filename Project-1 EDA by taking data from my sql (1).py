#!/usr/bin/env python
# coding: utf-8

# In[6]:


#pip install mysql-connector-python


# Data Mining from mysql

# In[7]:


import mysql.connector


# In[8]:


#conncet to server
cnx=mysql.connector.connect(
   host="127.0.0.1",
   port=3306,
   user="root",
   password="Althaf@1")


# In[11]:


import pandas as pd
con=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Althaf@1",
    database="Studmarks")

df=pd.read_sql_query("select *from Student_marks",con)
df


# Applying EDA process

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[13]:


df=pd.read_csv('Student_marks.csv')
df.head()


# In[14]:


df.shape


# In[15]:


df.dtypes


# In[16]:


df.columns


# In[17]:


df.info()


# summary statistics

# In[18]:


df.describe()


# key observations: 
# 1 The mean is more than median (50th percentile) in all columns except civics Right skewed data is present
# 
# 2 There is a large difference in 75% percentile and max in Maths,civics
# 
# 3 The 1 and 2 observations suggest that there are extreme outliers present in these three columns

# Data visualizations
To checking missing values
# In[28]:


sns.heatmap(df.isnull())


# Dataset has no missing values.
# 

# To check correlation

# In[30]:


dfcor=df.corr()
dfcor


# In[31]:


sns.heatmap(dfcor)


# In[32]:


get_ipython().run_line_magic('pinfo', 'sns.color_palette')


# In[33]:


get_ipython().run_line_magic('pinfo', 'sns.heatmap')


# In[34]:


plt.figure(figsize=(6,4))
sns.heatmap(dfcor,cmap='Blues',annot=True)

observations
Dark shades are highly correlated
# In[36]:


get_ipython().run_line_magic('pinfo', 'sns.heatmap')

cmap : matplotlib colormap name
colormap gives
# In[41]:


plt.figure(figsize=(10,6))
sns.heatmap(dfcor,cmap='YlOrRd_r',annot=True)

observations
Dark shades are highly correlated
# In[46]:


get_ipython().run_line_magic('pinfo', 'sns.heatmap')

cmap : matplotlib colormap name
colormap gives
# In[49]:


plt.figure(figsize=(10,6))
sns.heatmap(dfcor,cmap='YlOrRd_r',annot=True)

plotting outliers
# In[50]:


df.columns


# In[51]:


#univariate analysis
df['Maths'].plot.box()


# In[53]:


df['Physics'].plot.box()


# In[54]:


df['Chemistry'].plot.box()


# In[55]:


df['English'].plot.box()


# In[56]:


df['Biology'].plot.box()


# In[57]:


df['Economics'].plot.box()


# In[58]:


df['History'].plot.box()


# In[59]:


df['Civics'].plot.box()


# In[60]:


df.shape


# In[63]:


collist=df.columns.values
ncol=11
nrows=10


# In[64]:


get_ipython().run_line_magic('pinfo', 'plt.subplot')

