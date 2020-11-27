import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
import sys
import json
import PIL
from pip._vendor import requests
from PIL import Image
import urllib.request




def app():
    st.write('Welcome to our APP')

    # Local db info
    host = "localhost"
    user = "dsci551"
    password = "dsci551"
    database = "dsci551_project"

    def getConnection(host, user, password, database):
        db = mysql.connector.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database)
        return db

    def getProductInfo(word):
        # give a query word and return a list of product information
        db = getConnection(host, user, password, database)
        cursor = db.cursor(buffered=True)
        query = (
            "SELECT DISTINCT ProductId, title, listing_url, medium_image FROM amazon_product WHERE title LIKE '%{}%'".format(
                word))
        cursor.execute(query)
        return list(cursor.fetchall())

    def getProductReviews(ProductId):
        # take in productId and get the product review
        db = getConnection(host, user, password, database)
        cursor = db.cursor(buffered=True)
        query = ("SELECT  text FROM amazon_product WHERE ProductId = '{}'".format(ProductId))
        cursor.execute(query)
        return list(cursor.fetchall())

    def getProductScore(ProductId):
        # taka in ProductId and get the average score of the product
        db = getConnection(host, user, password, database)
        cursor = db.cursor(buffered=True)
        query = (
            "SELECT  ProductId, AVG(score) as AverageScore FROM amazon_product WHERE ProductId = '{}' GROUP BY ProductId".format(
                ProductId))
        cursor.execute(query)
        return list(cursor.fetchall())

    st.sidebar.header('Search')
    options = st.sidebar.text_input('What snack are you looking for?')

    if options:
        data = getProductInfo(options)
        st.title('Here are search results from Amazon for '+ options+':')
        st.write(len(data),'results found in total')

        # print out the product details
        for i in data:
            st.write('''##''', '''**''', i[1], '''**''')
            st.write('Product ID:', i[0])
            st.write('URL: ', i[2])
            im = Image.open(urllib.request.urlopen(i[3]))
            st.image(im, caption=i[1], width=300)
            score = getProductScore(i[0])
            st.write('Average Score for this product:', float(score[0][1]))
            st.write('Here are some reviews below:')
            reviews = getProductReviews(i[0])
            for i in range(5):
                st.write('''>''', reviews[i][0])
            st.write('Showing 5 review out of',len(reviews),'reviews')
            st.write(''' --- ''')
    else:
        st.write('Try search something!')

