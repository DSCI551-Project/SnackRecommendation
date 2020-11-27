import streamlit as st
import json
from pip._vendor import requests
import sys
import pandas as pd


def app():

    st.title('Here is our Food Nutrition Data')
    st.write('Take a look!')

    # firebase link to Open Food Fact dataset
    firebaseLink = "https://dsci551-openfoodfact.firebaseio.com/"

    allInfo = requests.get('%sopenFoodFact.json' % firebaseLink)
    allInfo = allInfo.json()

    st.json(allInfo)
