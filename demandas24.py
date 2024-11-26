import streamlit as st
import pandas as pd

st.title('Demandas TCU')
df = pd.read_excel('https://github.com/aprost20/testesDash/blob/main/Demandas2024.xlsx')

