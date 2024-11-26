import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def carregar_arquivo():
    arquivo = st.file_uploader("/content/Demandas2024.xlsx", type=["xlsx"])
    if arquivo is not None:
        df = pd.read_excel(arquivo)
        return df
    return None


