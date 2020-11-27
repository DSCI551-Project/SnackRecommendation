import streamlit as st
import pandas as pd
import numpy as np


def app():

    st.title('Here is our Amazon Product Data')
    st.write('Take a look!')

    APdata = pd.read_csv('amazon_product.csv',delimiter=';',header = 0)
    pd.set_option('display.max_colwidth', None)
    st.write(APdata)