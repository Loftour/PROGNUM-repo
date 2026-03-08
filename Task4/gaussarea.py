#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import scipy 
A = float(input('vale of the amplitude = '))
x0 = float(input('value of the peak = '))
sig = float(input('vale of width = '))
z0 = float(input('value of the offset = '))
a = float(input('value of the lower limit = '))
b = float(input('value of the upper limit = '))
x=np.linspace(-10,10,200)
def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0
y=gauss(x, A, x0, sig, z0)
plt.plot(x,y)
X=np.linspace(a,b,200)
k=gauss(X, A, x0, sig, z0)
Y, fake=scipy.integrate.quad(gauss,a,b,args=(A,x0,sig,z0))
plt.fill_between(X,k,y2=0)
plt.plot(x, y,color='black', label=f'area of bounds = {Y:.3f}')
plt.title("Gaussian Function and Integration Area")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

inf, fake=scipy.integrate.quad(gauss,-np.inf,np.inf,args=(A,x0,sig,z0))
print(f"area between infiniteies is {inf:.2f}")


# In[ ]:




