#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


from datetime import datetime


# In[4]:


name = input("Name: ")


# In[5]:



message = input("Comment: ")


# In[6]:


guestbook_entry = name + " - " + message


# In[7]:


guestbook_entry


# In[8]:


dateTimeObj = datetime.now()


# In[9]:


dateTimeObj


# In[10]:


timestampStr = dateTimeObj.strftime("%b-%d-%Y")


# In[11]:


timestampStr


# In[12]:


def guest_book1():
    for name in guestbook_entry:
        name_1 = input("Name: ")
        message_1 = input("Comment:  ")
        guestbook_entry1 = name_1 + " - " + message_1 +" " +  timestampStr
        print(guestbook_entry1)
        
        
        
    


# In[13]:


def comment():
    for name_2 in guestbook_entry1:
            name_2 =input("Name: ")
            message_2= input("Comment: ")
            return "@" + name_1 + " "+ message_2 + " - " + name_2 + timestampStr


# In[14]:


def input_comment():
    comment("Do you want to comment? Y or N?")
        


# In[15]:


#while True:
    #print("Welcome to the Guestbook!")
    #guest_book1()
    #input_comment()
#if input_comment().lower()=="y":
    #comment()
#else:
    #guestbook1()
    #input_comment()


# In[ ]:


while True:
    print("Welcome to the Guestbook!")
    for name in guestbook_entry:
        name_1 = input("Name: ")
        message_1 = input("Comment:  ")
        guestbook_entry1 = name_1 + " - " + message_1 +" " +  timestampStr
        print(guestbook_entry1)
        comment_0 = input("Do you want to comment? Y or N? ")
        if comment_0.lower() == "y":
            for name_2 in guestbook_entry1:
                name_2 =input("Name: ")
                message_2= input("Comment: ")
                print( "@" + name_1 + " "+ message_2 + " - " + name_2 + " " + timestampStr)
                start_new_thred = input("Do you want to start a new thred or keep commenting? T or C? ")
                if start_new_thred.upper() == "T":
                    guest_book1()      
                elif start_new_thred.upper() == "C":
                    for name_2 in guestbook_entry1:
                        name_2 =input("Name: ")
                        message_2= input("Comment: ")
                        print("@" + name_2 + " "+ message_2 + " - " + name_2 + timestampStr)


# In[ ]:





# In[ ]:




