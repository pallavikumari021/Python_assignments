#!/usr/bin/env python
# coding: utf-8

# Write a Python Program to Find the Factorial of a Number?

# In[3]:


def fact(n):
    return 1 if(n==1 or n==0) else n*fact(n-1);
num=int(input())
print("Factorial of",num,"is", fact(num))  


# Write a Python Program to Display the multiplication Table?

# In[5]:


num=int(input())
for i in range(1, 11):
    print(num,'x', i, '=', num*i)


# Write a Python Program to Print the Fibonacci sequence?

# In[1]:


n_terms = int(input ("How many terms the user wants to print? "))  
   
n_1 = 0  
n_2 = 1  
count = 0  
  
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  

elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
        n_1 = n_2  
        n_2 = nth  
        count += 1 


# Write a Python Program to Check Armstrong Number?

# In[7]:


num = int(input("Enter a number: "))

sum = 0
n1 = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n1
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# Write a Python Program to Find Armstrong Number in an Interval?

# In[9]:


lwr=100
uppr=2000
for num in range(lwr, uppr+1):
    n1=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit = temp%10
        sum+=digit**n1
        temp//=10
    if num==sum:
        print("The Armstrong numbers are: ",num)


# Write a Python Program to Find the Sum of Natural Numbers?

# In[2]:


num=int(input("Enter number upto which you want the sum"))
if num<0:
    print("Enter positive number")
else:
    sum=0
    while(num>0):
       sum += num  
       num -= 1  
    print(sum)
        


# In[ ]:





# In[ ]:




