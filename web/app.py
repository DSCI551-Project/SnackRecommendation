import app1
import app2
import app3
import app4
import home
import streamlit as st


PAGES = {
    "Home": home,
    "Amazon Results": app1,
    "Nutrition Results": app2,
    "Amazon Raw Data": app3,
    "Food Nutrition Raw Data": app4
}



st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()



