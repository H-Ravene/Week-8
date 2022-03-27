#!/usr/bin/env python
# coding: utf-8

# In[7]:


# In this jupyter notebook we are going to be loading a dataset, performing some minor cleanup and transformation tasks, then using exploratory data analysis to learn about the distribution of variables and the relationships between variables.
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import pandas as pd

#Loading the data in the into a pandas DataFrame
pd.set_option('display.notebook_repr_html',True) 
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None) 
mpg = pd.read_csv(r"file:///C:/Users/Sixpm/Downloads/auto-mpg.data", header=None, delim_whitespace=True)
mpg.head(5)
#Using the attribute information provided to name our pandas DataFrame columns.
mpg.rename(columns={0: 'mpg',                     1: 'cylinders',                     2: 'displacement',                     3: 'horsepower',                     4: 'weight',                     5: 'acceleration',                     6: 'model_year',                     7: 'origin',                     8: 'car_name',}, inplace=True)
#Some of the horsepower data is marked as missing with a ‘?’. We are going to replace this ‘?’ with a pandas-appropriate missing value, then we will convert the column to numeric.
mpg.horsepower.replace('?', np.nan, inplace=True)
mpg.horsepower = mpg.horsepower.astype(np.float)
mpg.dtypes
#Converting the origin column values to  to ‘USA’,‘Asia’, and ‘Europe’ respectively. 
mpg.origin.replace([1,2,3], ['USA','Asia','Europe'], inplace=True)
mpg
#Creating  a bar chart that shows the distribution for cylinders.
a = sns.countplot(x="cylinders", hue='origin' ,data=mpg)
plt.xlabel("Cylinders",size = 20)
plt.ylabel("Count",size = 20)
#Creating a scatterplot that shows the relationship between horsepower and weight.
b = sns.regplot(x="horsepower", y="weight", data=mpg, color='m')
plt.title('The relationship between horsepower and weight', fontsize=20)
plt.xlabel("Horsepower",size = 15)
plt.ylabel("Weight",size = 15)
#Figuring out whether MPG changes over time and whether the country of origin makes a difference
c = sns.lmplot(x='model_year', y='mpg', hue='origin', data=mpg)
plt.title('MPG over Time by Origin', fontsize=22)
plt.xlabel('Model Year', fontsize=15)
plt.ylabel('Miles Per Gallon', fontsize=15)


# In[ ]:




