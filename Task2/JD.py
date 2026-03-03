#!/usr/bin/env python
# coding: utf-8

# In[6]:


Y=float(input("year ="))
M=float(input("month ="))
D=float(input("day ="))
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"the day number is {JD}")
y=float(input("year ="))
m=float(input("month ="))
d=float(input("day ="))
jd = 367*y -7*(y+(m+9)//12)//4 - 3*((y+(m-9)//7)//100 + 1)//4 + (275*m)//9 + d + 1721029-0.5
diff=JD-jd
print(f"the difference between the 2 dates is {diff}")

