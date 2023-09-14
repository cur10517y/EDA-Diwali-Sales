#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np              # importing python libraries
import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'C:\Users\user\Desktop\Diwali_Sales_DataSet.csv', encoding= 'unicode_escape')  # importing csv file


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)    #dropping blank columns


# In[7]:


pd.isnull(df).sum()   #check for null values


# In[8]:


df.dropna(inplace=True)   # dropping null values


# In[9]:


df['Amount'] = df['Amount'].astype('int') # changing data type


# In[10]:


df['Amount'].dtypes


# In[11]:


df.columns  # column names


# In[12]:


df.rename(columns= {'Marital_Status':'Marriage_Status'})    #renaming column name


# In[13]:


df.describe()


# In[14]:


df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ### Gender

# In[15]:


# Gender vs Count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[16]:


# Gender vs Total Amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# *From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men*

# ### Age

# In[17]:


# Gender wise Age Group vs Count

ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


# Total Amount vs Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*

# ### State

# In[19]:


# Total number of Orders from Top 10 States

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[20]:


# Total Amount of Sales from Top 10 States

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# *From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*
# 

# ### Marital Status

# In[21]:


# Marital_Status vs Count

ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


# Gender wise Marital_Status vs Amount

sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# ### Occupation

# In[23]:


# Occupation vs Count

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


# Occupation vs Amount

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# ### Product Category

# In[25]:


# Product Category vs Count

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


# Product Category vs Amount

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# In[27]:


# Product ID vs Orders

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# Conclusion:
# Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
