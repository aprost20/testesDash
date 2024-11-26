import pandas as pd

# Substitua pelo caminho correto do arquivo
file_path = "Demandas2024.xlsx"
try:
    data = pd.read_excel(file_path)
    print(data.head())
except Exception as e:
    print("Erro ao carregar o arquivo Excel:", e)
 


