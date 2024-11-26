import streamlit as st
import pandas as pd
import requests as req

st.title('Demandas TCU 2024 recebidas pelo MPO')
uploaded_file = st.file_uploader("/content/Demandas2024.xlsx", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, engine='openpyxl')

st.subheader('Visão geral dos dados')
st.write(df.head())

