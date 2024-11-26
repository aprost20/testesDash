import streamlit as st
import pandas as pd

st.title('Demandas TCU 2024 recebidas pelo MPO')
df = pd.read_xlsx('Demandas2024.xlsx')

