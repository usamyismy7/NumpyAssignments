#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[2]:


import numpy as np
data = np.arange(10)
data = data.reshape(2,5)
data


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[15]:


data1 = np.arange(10).reshape(2,5)
data2 = np.arange(10,20).reshape(2,5)
print(np.vstack((data1,data2)))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[16]:


data1 = np.arange(10).reshape(2,5)
data2 = np.arange(10,20).reshape(2,5)
print(np.hstack((data1,data2)))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[8]:


data = np.arange(20).reshape(4,5)
print(data)
print(data.ravel())


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[7]:


import numpy as np
data = np.arange(18).reshape(3,3,2)
print(data)
print(data.ravel())


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[11]:


data = np.arange(18)
data = data.reshape(3,3,2)
data


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[21]:


a = np.random.rand(5,5)*100
print(np.square(a))


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[24]:


data = np.random.randint(1,9, size=(5,6))
print(data)


# In[25]:


print(np.mean(data))


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[27]:


data = np.random.randint(1,9,size=(5,6))
print(np.std(data))


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[28]:


data = np.random.randint(1,9,size=(5,6))
print(np.median(data))


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[30]:


data = np.random.randint(1,9,size=(5,6))
print(data)
print(data.transpose())


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[32]:


data = np.random.randint(1,9,size=(4,4))
print(data,np.trace(data))


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[33]:


data = np.random.randint(1,9,size=(4,4))
print(np.linalg.det(data))


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[38]:


import numpy as np
data = np.arange(100)
print(np.percentile(data,5))
print(np.percentile(data,95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[40]:


a = np.identity(3)
a[0,0] = None
print(np.isnan(a))


# In[ ]:




