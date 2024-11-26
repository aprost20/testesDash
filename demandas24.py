pip install streamlit pandas openpyxl

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = "Demandas2024.xlsx"
data = pd.read_excel(file_path)
print(data.head())

