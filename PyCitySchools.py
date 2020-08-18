#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add the Pandas dependency.
import pandas as pd


# In[2]:


# Files to load
school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"


# In[3]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[4]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[ ]:




