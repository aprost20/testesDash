import streamlit as st
import pandas as pd

st.title("Carregar e Visualizar Dados do Excel")

uploaded_file = st.file_uploader("Carregue sua planilha Excel", type="xlsx")

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.write("Visualização dos dados:")
    st.write(data.head())

 


