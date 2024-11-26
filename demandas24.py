import streamlit as st
import pandas as pd

st.title('Demandas TCU recebidas pelo MPO em 2024')
df = pd.read_excel('/content/Demandas2024.xlsx')

demandas = df['Estado do SISCOD'].unique()
demandasFiltro = st.selectbox('Selecione o status da demanda', demandas)
dadosFiltrados = df[df['Estado do SISCOD'] == demandasFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
