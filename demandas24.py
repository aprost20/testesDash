import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Carregue sua planilha Excel", type="xlsx")
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.write(data.head())

