#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find sum of elements in list?

# In[1]:


l = [4, 8, 9, 10]
print(sum(l))


# In[3]:


list = [2,4,2,5,7,9,23,4,5]
sum=0
for i in list:
    sum+=i
print('Sum of List: ', sum)


# 2. Write a Python program to Multiply all numbers in the list?

# In[7]:


list = [2, 4, 3, 1,8]
Product=1
for i in list:
    Product*=i
print('Product of List: ', Product)


# 3. Write a Python program to find smallest number in a list?

# In[11]:


list = [2, 4, 6, -9]
min = list[0]

#find the smallest 
for i in range (len (list)):
  if list[i] < min:
    min = list[i]
print ("The smallest element is ", min)


# 4. Write a Python program to find largest number in a list?

# In[13]:


list = [2, 8, 56, -9]
max = list[0]

#find the largest 
for i in range (len (list)):
  if list[i] > max:
    max = list[i]
print ("The smallest element is ", max)


# 5. Write a Python program to find second largest number in a list?

# In[14]:


list = [20, 30, 40, 25, 10]  

# sorting the list  
list.sort() 

#displaying the second last element of the list  
print("The second largest element of the list is:", list_val[-2])  


# 6. Write a Python program to find N largest elements from a list?

# In[15]:


List = [120, 50, 89, 170, 45, 250, 450, 340]

print("List = ",List)

n = 4

#sort the List
List.sort()

# the largest N integers from the list
print("Largest integers from the List = ",List[-n:])


# 7. Write a Python program to print even numbers in a list?

# In[1]:


def even(list):
    new_list=[]
    for i in list:
        if i%2==0:               
            new_list.append(i)
    return new_list

li=[2, 4, 3, 2, 1]

print("Even numbers in ",li)
print(even(li))


# 8. Write a Python program to print odd numbers in a List?

# In[2]:


def odd(list):
    new_list=[]
    for i in list:
        if i%2!=0:               
            new_list.append(i)
    return new_list

li=[2, 4, 3, 2, 1]

print("Odd numbers in ",li)
print(odd(li))


# 9. Write a Python program to Remove empty List from List?

# In[3]:


list1 = [[], [], [], [], [], '2', '3', [], '4']
list2 = []
for item in list1:
    if item!=[]:
        list2.append(item)
print(list2)


# 10. Write a Python program to Cloning or Copying a list?

# In[3]:


original_list = [10, 22, 44, 23, 4]

new_list = list(original_list)

print(original_list)

# Print the contents of the 'new_list', which is a copy of 'original_list'
print(new_list)


# 11. Write a Python program to Count occurrences of an element in a list?

# In[1]:


list = []
n = int(input("Enter the size of the list "))
for i in range(0, n):
    e = int(input("Enter the element of the list "))
    list.append(e)
print("Original list: ", list)
t = int(input("Enter the element whose occurrences: "))
print(t, "has occurred", list.count(t), "times")

