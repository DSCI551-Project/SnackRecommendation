import streamlit as st
import json
from pip._vendor import requests
import sys
import pandas as pd
import matplotlib.pyplot as plt


def app():

    st.sidebar.header('Search')
    options = st.sidebar.text_input('What snack are you looking for?')

    st.write('Welcome to our APP')


    # firebase link to Open Food Fact dataset
    firebaseLink = "https://dsci551-openfoodfact.firebaseio.com/"

    def getAllInfo(searchWord):
        '''this function takes in a string as the search keyword and returns a pandas dataframe with all products' information that matches the search word (sorted based on nutrition score)'''
        allInfo = requests.get('%sopenFoodFact.json?orderBy="$key"&equalTo="%s"' % (firebaseLink, searchWord))
        allInfo = allInfo.json()
        result = []
        col_names = ['brands', 'carbohydrates_100g', 'countries_en', 'energy_100g', 'fat_100g', 'fiber_100g',
                     'ingredients_text', 'nutrition-score-uk_100g', 'product_name', 'proteins_100g', 'salt_100g',
                     'serving_size', 'sugars_100g', 'url', 'vitamin-c_100g']
        for idx in allInfo[searchWord]:
            productInfo = allInfo[searchWord][idx]  # info for each product
            productList = []
            for category in productInfo:
                productList.append(productInfo[category])
            result.append(productList)
        resultDF = pd.DataFrame(result, columns=col_names)
        # reorder the columns for displaying purpose
        resultDF = resultDF[
            ['product_name', 'brands', 'serving_size', 'nutrition-score-uk_100g', 'energy_100g', 'carbohydrates_100g',
             'fat_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sugars_100g', 'vitamin-c_100g',
             'ingredients_text', 'url']]
        resultDF.sort_values(by='nutrition-score-uk_100g', ascending=False, inplace=True)
        return resultDF

    def getTopTenInfo(resultDF):
        '''this function takes the search result from function getAllInfo and return the top ten products based on nutrition score, return all products if the results contains less than ten products'''
        return resultDF.head(10)

    def getNumCols(resultDF):
        '''takes in the result dataframe and returns all the numeric columns of the result dataframe'''
        num_cols = ['nutrition-score-uk_100g', 'energy_100g', 'carbohydrates_100g', 'fat_100g', 'fiber_100g',
                    'proteins_100g', 'salt_100g', 'sugars_100g', 'vitamin-c_100g']
        num_result = resultDF[num_cols]
        return num_result

    def getAvgInfo(resultDF):
        '''this function takes the search result from function getAllInfo and returns the average of each numeric column that matches the search word in a pandas dataframe'''
        # resultDF = getAllInfo(searchWord)
        # print(resultDF.columns)
        # num_cols = [ 'nutrition-score-uk_100g', 'energy_100g', 'carbohydrates_100g', 'fat_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sugars_100g', 'vitamin-c_100g']
        # num_result = resultDF[num_cols]
        num_result = getNumCols(resultDF)
        average_df = num_result.mean(axis=0).to_frame()
        average_df.rename(columns={0: "Average"}, inplace=True)
        return average_df.T

    def getDetails(resultDF):
        '''takes the search result from function getAllInfo and return the max, 3q, med, 1q, min'''
        # resultDF = getAllInfo(searchWord)
        num_result = getNumCols(resultDF)
        max_list = num_result.max(axis=0)
        col_names = max_list.index
        print(col_names)
        max_list = max_list.to_list()
        upperQ_list = num_result.quantile(q=0.75, axis=0).to_list()
        med_list = num_result.median(axis=0).to_list()
        lowerQ_list = num_result.quantile(q=0.25, axis=0).to_list()
        min_list = num_result.min(axis=0).to_list()
        detail = {'max': max_list, 'third_quartile': upperQ_list, 'median': med_list, 'first_quartile': lowerQ_list,
                  'min': min_list}
        detail = pd.DataFrame(data=detail, index=col_names).T

        return detail

    def getBoxPlotOther(resultDF):
        '''this function takes the search result from function getAllInfo and draw the boxplot of each numeric column (excluding energy col)'''
        # resultDF = getAllInfo(searchWord)
        num_cols = ['nutrition-score-uk_100g', 'carbohydrates_100g', 'fat_100g', 'fiber_100g', 'proteins_100g',
                    'salt_100g', 'sugars_100g', 'vitamin-c_100g']
        num_result = resultDF[num_cols]
        return num_result
        #num_result.boxplot()
        #plt.show()

    def getBoxPlotEnergy(resultDF):
        '''this function takes the search result from function getAllInfo and draw the boxplot of the energy column'''
        # resultDF = getAllInfo(searchWord)
        num_cols = ['energy_100g']
        num_result = resultDF[num_cols]
        return num_result
        #num_result.boxplot()
        #plt.show()

    if options:
        st.title('Here are search results for Nutrition Facts for '+ options+':')


        resultDF = getAllInfo(options)
        tten = getTopTenInfo(resultDF)

        st.bar_chart(getBoxPlotOther(tten))

        avginf = getAvgInfo(resultDF)
        st.write('''##''', '''**''', 'Average nutrition information:', '''**''')
        st.table(avginf)


        st.write('''##''', '''**''', 'Top products nutrition details:', '''**''')
        st.table(tten)

        dtten = getDetails(tten)
        st.write('''##''', '''**''', 'Top products nutrition ranking:', '''**''')
        st.table(dtten)

    else:
        st.write('Try search something!')

