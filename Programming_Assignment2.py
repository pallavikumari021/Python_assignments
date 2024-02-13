#!/usr/bin/env python
# coding: utf-8

# Write a Python program to convert kilometers to miles?

# In[1]:


kilometer=float(input("Enter Km value"))
conv_ratio=0.621371
miles= kilometer*conv_ratio
print("The speed of the car in miles", miles)


# Write a Python program to convert Celsius to Fahrenheit?

# In[3]:


celsius=int(input())
Fahrenheit = (1.8 * celsius) + 32
print("Temperature in fahrenheit", Fahrenheit)


# Write a Python program to display calendar?

# In[4]:


import calendar
year =int(input("Enter year "))
month = int(input("Enter month "))
print(calendar.month(year, month))


# Write a Python program to solve quadratic equation?

# In[5]:


import cmath
a=float(input())
b=float(input())
c=float(input())
d = (b**2) - (4*a*c)  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   


# Write a Python program to swap two variables without temp variable?

# In[6]:


a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print("a is", a, "b is", b)

