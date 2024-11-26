import pandas as pd
data = pd.read_excel('/content/Demandas2024.xlsx') 

import streamlit as st
import pandas as pd

# Carregar dados do Excel
data = pd.read_excel('/content/Demandas2024.xlsx')

# Exibir título
st.title('Análise de Dados do Excel')

# Exibir tabela de dados
st.dataframe(data)


st.line_chart(data['especie'])

