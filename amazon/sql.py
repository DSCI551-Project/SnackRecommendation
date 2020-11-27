#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import sys
import json


# In[16]:
# may have to change to your local db setting 

host = "localhost"
user = "dsci551"
password = "dsci551"
database = "dsci551_project"



# In[21]:


def getConnection(host, user, password, database):
    db = mysql.connector.connect(host=host,
                             user=user,
                             password=password,
                             database=database)
    return db


# In[50]:


def getProductInfo(word):
    # give a query word and return a list of product information 
    db = getConnection(host, user, password, database)
    cursor = db.cursor(buffered = True)
    query = ("SELECT DISTINCT ProductId, title, listing_url, medium_image FROM amazon_product WHERE title LIKE '%{}%'".format(word))
    cursor.execute(query)
    return list(cursor.fetchall())


# In[47]:


def getProductReviews(ProductId):
    # take in productId and get the product review 
    db = getConnection(host, user, password, database)
    cursor = db.cursor(buffered = True)
    query = ("SELECT  text FROM amazon_product WHERE ProductId = '{}'".format(ProductId))
    cursor.execute(query)
    return list(cursor.fetchall())


# In[41]:


def getProductScore(ProductId):
    # taka in ProductId and get the average score of the product 
    db = getConnection(host, user, password, database)
    cursor = db.cursor(buffered = True)
    query = ("SELECT  ProductId, AVG(score) as AverageScore FROM amazon_product WHERE ProductId = '{}' GROUP BY ProductId".format(ProductId))
    cursor.execute(query)
    return list(cursor.fetchall())


# In[42]:


print(getProductScore('B000HDOPZG'))


# In[48]:


print(getProductReviews('B000HDOPZG'))


# In[52]:


print(getProductInfo("CAKE"))


# In[ ]:




