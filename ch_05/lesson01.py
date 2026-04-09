#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *


# In[2]:


x = symbols('x')


# In[3]:


diff(x ** 3 + 2 * x** 2 + sin(x))


# In[4]:


a,b,c,u,v = symbols('a b c u v')


# In[5]:


diff(a*x**2 + b*x + c, x)


# In[6]:


diff(a*u**2 + b*v**2*u + c, u)


# In[7]:


diff(a*u**2 + b*v**2*u + c, v)


# In[8]:


diff(a*u**2 + b*v**2*u + c, u, v)


# In[ ]:




