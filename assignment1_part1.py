#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""  IS211_Assignment1 """

def listDivide(numbers, divide = 2):
    """Function with parameters: list numbers and  int divide"""
    mylist = []
    for number in numbers:
        if number % divide ==0:
             mylist.append(number)
    return len(mylist)
    

class ListDivideExceptio(Exception):
    
    pass
    
    
def testListDivide():
    
    
    tests = [
        ([1,2,3,4,5]),
        ([2,4,6,8,10]),
        ([30, 54, 63,98, 100]),
        ([]),
        ([1,2,3,4,5], 1)
        ]
    for numbers in tests:
        if listDivide != divide:
            raise ListDivideException( "Raise Alarm" )
    
        
        


# In[2]:


listDivide([1,2,3,4,5])


# In[4]:


listDivide([2,4,6,8,10])


# In[5]:


listDivide([30, 54, 63,98, 100], divide=10)


# In[7]:


listDivide([])


# In[8]:


listDivide([1,2,3,4,5], 1)


# In[ ]:




