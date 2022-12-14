import streamlit as st
import numpy as np
import pandas as pd
st.title('My first app')
st.write('this is table')
netflix_data = pd.read_csv('netflix_titles.csv')
st.write(netflix_data)

st.line_chart(netflix_data)

st.write('This is a area_chart.')
st.area_chart(netflix_data)

st.write('This is a bar_chart.')
st.bar_chart(netflix_data)

