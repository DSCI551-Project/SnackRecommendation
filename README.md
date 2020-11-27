# Recommendation System for Snacks

Created by: Cheng Peng, Lishi Ji, Zixin Zhang

Please check out our demo video: https://usc.zoom.us/rec/share/QrI0p1Lp06OJEBefHGl21LbOPc1IUBOLPUQ16QiYKJu81_JTtQq9o3EAyAW6Iv9Z.ct1MzAFw9CgSs12f?startTime=1606357341000

## web
All files on website are included under this folder.

#### Procedure of Installation and Lauching:
First download streamlit package:  
$ pip install streamlit  

Download all the python files in one folder and then run the command where the python files located:  
$ streamlit run app.py. 

The website will pop up automatically.   


## amazon
All files on amazon datbase, our first database(stored in SQL) used in the project, are included under this folder.

#### Explaination of each file:  
product search result.pdf: example output format   
sql.py: SQL query to get data from the database  
query keywords.txt: sample keywords for search
amazon_product_ver2.csv: the latest version of the cleaned dataset. 
amazon_product.csv: an old version of the cleaned dataset. 

## openFoodFact
All files on Open Food Facts datbase, our second database(stored in Firebase) used in the project, are included under this folder.

#### Explaination of each file:  
openFoodFactSpark.py: the process of data cleaning using Spark  
openFoodFactConcise.json: data uploaded to firebase  
firebase.py: code to get data from firebase with requests package.   
openFoodFact_keywords.txt: all keywords (categories) included in the dataset   

## taquitos (not used)
Process of exploring taquitos.com and code for scraping data, but this dataset is not included in the final version of our project due to the incompleteness of web scraping.

