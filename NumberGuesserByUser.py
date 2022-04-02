#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Guess the number by computer
import random

def guess(x):
    random_number = random.randint(1, x)
    guess=0
    while guess != random_number:
        guess =int(input("Enter a number between 1 and x : "))
        if guess < random_number :
            print("Sorry , guess again, too low ")
        elif guess > random_number :
            print("Sorry , too high")
    print("Yayy , Congrats ,You got it")
    
    
        
guess(10)


# In[ ]:





# In[ ]:




