#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
a=float(input("a ="))
b=float(input("b ="))
c=float(input("c ="))
d=(b**2)-(4*a*c)
if d<0:
        print("no real values")
else:
        x_1=(-b+np.sqrt(d))/(2*a)
        x_2=(-b-np.sqrt(d))/(2*a)
        print(f"x_1 = {x_1} and x_2 = {x_2}")


# In[ ]:




