#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
x=range(-5,6)
y=np.cosh(x)
import matplotlib.pyplot as plt
plt,ax=plt.subplots()
ax.set_title("caternary plot")
ax.plot(x,y,color="red",label="catenary")
ax.legend()
plt.show()


# In[ ]:




