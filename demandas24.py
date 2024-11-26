import streamlit as st
import pandas as pd
import requests as req

st.title('Demandas TCU recebidas pelo MPO em 2024')
df = pd.read_csv('/content/Demandas2024.csv')

