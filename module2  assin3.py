#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 MAX OF THREE


# In[5]:


n1=float(input("enter he first number"))
n2=float(input("enter the second number"))
n3=float(input("enter the thrid number"))
if (n1>n2)and(n1>n1):
    print("n1 is greater")
elif (n2>n1)and(n2>n3):
    print("n2 is greater")
else:
    print("n3 is greater")


# In[6]:


#2 REVERSE OF A STRING


# In[8]:


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('apple'))


# In[9]:


#3 PALINDROME


# In[5]:


def palindrome():
        try:   
            num=int(input("enter a number :"))
            rev=0
            num1=num
            while(num>0):
                rem=num%10
                rev=(rev*10)+rem
                num=num//10
            if(num1==rev):
                print("YES ITS A PALINDROME..")
            else:
                print("NO ITS NOT A PALINDROME..")
            
        except:
            print("please enter valid input..")
        finally:
            print("done")


# In[7]:


palindrome()


# In[8]:


#4


# In[9]:


def prime():
    
    a=int(input("enter a number:"))
    
    for i in range(2,a):
        if(a%i==0):
            j=1
            break
        else:
            j=0
       
    if(j==1):
        print("not a prime")
    else:
        print("yes its a prime")


# In[10]:


prime()


# In[11]:


#5


# In[7]:


def sumOfSquares():
    
    a=int(input("enter an number :"))
    sum=0
    b=a+1
    for i in range(1,b):
        sum=sum+(i**2)
    print("sum is ",sum)


# In[9]:


sumOfSquares()


# In[ ]:




