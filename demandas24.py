import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = "Demandas2024.xlsx"  # Substitua pelo caminho correto
data = pd.read_excel(file_path)

# Obter a contagem de valores na coluna "status"
status_counts = data['status'].value_counts()

# Configurar o título do app no Streamlit
st.title("Análise de Status das Demandas")

# Criar um gráfico de barras
st.subheader("Distribuição de Status")
fig, ax = plt.subplots()
status_counts.plot(kind='bar', color=['blue', 'green', 'orange', 'red'], ax=ax)
ax.set_title("Status das Demandas")
ax.set_xlabel("Status")
ax.set_ylabel("Quantidade")
st.pyplot(fig)

# Exibir os dados em tabela
st.subheader("Dados Brutos")
st.dataframe(data[['status']])

