#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[4]:


numpy.array([3,5,8,17])


# In[5]:


numpy.ones(5)


# In[6]:


numpy.zeros(5)


# In[15]:


numpy.arange(5)


# In[16]:


numpy.arange(6,12
        )


# In[17]:


numpy.arange(6,12,2)


# In[18]:


numpy.linspace(6,12,3)


# In[19]:


numpy.linspace(6,12)


# In[21]:


len(numpy.linspace(6,12))


# In[24]:


import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(a)
print("dimension of array=",arr.ndim)


# In[25]:


import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(a)
print("shape of array=",arr.shape)


# In[30]:


arr=np.ones((4,4))
arr


# In[36]:


arr=np.eye((3))
arr


# In[37]:


arr=np.eye(3,4)
arr


# In[38]:


arr=np.eye(3,4)
arr


# In[41]:


arr=np.diag([2,3,3,4])
np.diag(arr)


# In[44]:


arr=np.random.randint(1,10,3)
arr


# In[46]:


arr=np.random.rand(5)
arr


# In[47]:


arr=np.random.rand(2,3)
arr


# In[49]:


np.arange(0,100,6)


# In[50]:


Arr2=np.random.randint(10,size=(4,3))
Arr2


# In[52]:


Arr1=np.random.randint(20,size=(4,3))
Arr1


# In[53]:


Arr2=np.random.randint(10,size=(4,3))
Arr2


# In[54]:


Arr3=np.concatenate((Arr1,Arr2),axis=0) 
Arr3


# In[55]:


np.split(Arr3,2)


# In[56]:


np.hsplit(Arr3,3)


# In[92]:


Arr3


# In[58]:


Arr4=Arr3.reshape(3,8)
Arr4


# In[59]:


Arr3[0:5,2]


# In[60]:


Arr3>10


# In[61]:


Arr4


# In[62]:


np.add(Arr4,1)


# In[63]:


np.multiply(Arr4,2)


# In[64]:


Arr6=np.random.randint(5,size=(3,4))
Arr6


# In[67]:


Arr7=np.random.randint(15,size=(3,4))
Arr7


# In[91]:


np.add(Arr6,Arr7)


# In[68]:


Arr8=np.add(Arr6,1)
Arr8


# In[69]:


Arr9=np.add(Arr7,1)
Arr9


# In[70]:


Arr10=np.divide(Arr8,Arr9)
Arr10


# In[72]:


np.ceil(Arr10)


# In[74]:


np.mean(Arr9,axis=1)


# In[75]:


Arr9.min()


# In[76]:


Arr9.max()


# In[77]:


np.var(Arr9)


# In[80]:


np.std(Arr9,axis=1)


# In[88]:


a
Arr11=np.append(Arr8,(1,2,3,4))
Arr11


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




