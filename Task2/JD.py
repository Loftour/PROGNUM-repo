#!/usr/bin/env python
# coding: utf-8

# In[6]:


Y=float(input("year ="))
M=float(input("month ="))
D=float(input("day ="))
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"the day number is {JD}")

