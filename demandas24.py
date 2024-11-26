import streamlit as st
import pandas as pd
import requests as req

st.title('Demandas TCU 2024 recebidas pelo MPO')
uploaded_file = st.file_uploader("/content/Demandas2024.xlsx", type=["xlsx"])



