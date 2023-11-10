#!/usr/bin/env python
# coding: utf-8

# # Darris Femilia
# # Task3- Spark Foundation
# # Exploratory Data Analysis on Retail

# In[1]:


#import libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#load the data

data = pd.read_csv("C:/Users/HP/Downloads/SampleSuperstore.csv")
data.head()


# In[3]:


#dataset information

data.info()


# In[4]:


#display top 5 rows

data.head()


# In[5]:


#display last 5 rows

data.tail()


# In[6]:


#dimension

data.shape


# In[7]:


#statistics about the datest

data.describe()


# In[8]:


#checking null values

data.isnull().sum()


# In[9]:


data["Category"].value_counts()


# In[10]:


#profit by category

plt.figure(figsize=(12, 6))
sns.barplot(x="Category", y="Profit", data=data)
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.show()


# In[11]:


data["Sub-Category"].value_counts()


# In[12]:


#profit by subcategory

plt.figure(figsize=(14, 8))
sns.barplot(x="Sub-Category", y="Profit", data=data)
plt.title("Profit by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.xticks(rotation=90)
plt.show()


# In[13]:


data["Region"].value_counts()


# In[14]:


#profit by region

plt.figure(figsize=(12, 6))
sns.barplot(x="Region", y="Profit", data=data)
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()


# In[15]:


data["Ship Mode"].value_counts()


# In[16]:


#profit by shipmode

plt.figure(figsize=(10, 6))
sns.barplot(x="Ship Mode", y="Profit", data=data)
plt.title("Profit by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Profit")
plt.show()


# In[17]:


data["Segment"].value_counts()


# In[18]:


#profit by segment

plt.figure(figsize=(10, 6))
sns.barplot(x="Segment", y="Profit", data=data)
plt.title("Profit by Segment")
plt.xlabel("Segment")
plt.ylabel("Profit")
plt.show()


# In[19]:


#profit/discount

plt.figure(figsize=(12, 6))
sns.lineplot(x="Discount", y="Profit", data=data)
plt.title("Profit by Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()


# In[20]:


#sales vs profit

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Sales", y="Profit", data=data)
plt.title("Sales vs. Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()


# In[21]:


#correlation

correlation =data.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')


# In[ ]:


#total sales by state

state_sales_profit = data.groupby("State")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)
plt.figure(figsize=(16, 8))
sns.barplot(x=state_sales_profit.index, y=state_sales_profit["Sales"], data=state_sales_profit, palette="viridis")
plt.title("Total Sales by State")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#total profit by state

plt.figure(figsize=(16, 8))
sns.barplot(x=state_sales_profit.index, y=state_sales_profit["Profit"], data=state_sales_profit, palette="viridis")
plt.title("Total Profit by State")
plt.xlabel("State")
plt.ylabel("Total Profit")
plt.xticks(rotation=90)
plt.show()


# In[ ]:


#checking minimum and maximum profit

avg_profit = data.groupby("Discount")["Profit"].mean()
max_discount = avg_profit.idxmax()
min_discount = avg_profit.idxmin()

print(f"Maximum Average Profit at {max_discount} discount level")
print(f"Minimum Average Profit at {min_discount} discount level")

