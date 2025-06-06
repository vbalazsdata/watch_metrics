import pandas as pd
import streamlit as st

# Caching the Tw object to optimize performance
@st.cache_data(ttl=120)
def get_data():
    data=pd.read_csv('watchmetrics_data.csv')

    return(data)