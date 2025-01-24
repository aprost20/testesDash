import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Demandas TCU 2024", layout="wide")

# Carregamento do arquivo Excel
df = pd.read_excel('Demandas_2024_1.xlsx', sheet_name=0)
df2 = pd.read_excel('acordaos_atendidos_gestãoMPO_2.xlsx', sheet_name=0)


col1, col2 = st.columns([3,1])

with col2:
    st.image("MPOAssinatura.png", width = 300)

col1, col2 = st.columns([3,1])
with col1:
    st.title("Demandas TCU recebidas pelo MPO em 2024")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    quantidades_counts = df['estado_SISCOD'].value_counts().reset_index()
    quantidades_counts.columns = ['estado_SISCOD', 'quant_estado']
    fig1 = px.pie(quantidades_counts, values = 'quant_estado', names = 'estado_SISCOD', color_discrete_sequence= px.colors.qualitative.Light24)
    fig1.update_layout(title = 'Situação atual das demandas TCU (em quantidade de itens)')
    fig1.update_traces(textposition = 'inside', textinfo = 'value+label')
    st.plotly_chart(fig1, use_container_width = True)
   
with col2:
    tipo_demanda = df['tipo_processo'].value_counts()
    fig2 = px.bar(tipo_demanda, text_auto=True, color_discrete_sequence=['#183EFF'])
    fig2.update_layout(title='Demandas por tipo de Processo TCU', xaxis_title="Tipo de Processo", yaxis_title="Quantidade itens demandados") 
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
  qnt_dem_respons = df['responsavel'].value_counts()
  fig3 = px.bar(qnt_dem_respons, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig3.update_layout(title = 'Demandas por unidade do MPO', xaxis_title = "Unidade demandada", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig3, use_container_width = True)

with col4:
  filtro_prazo = df.query('no_prazo == "Sem_prazo" or no_prazo == "Em andamento" or no_prazo == "Atendida no prazo" or no_prazo == "Atendida com atraso"')
  quantidades_prazo = df['no_prazo'].value_counts().reset_index()
  quantidades_prazo.columns = ['no_prazo', 'valor_no_prazo']
  fig4 = px.bar(quantidades_prazo, x = 'no_prazo', y = 'valor_no_prazo', color = 'no_prazo', text_auto = True)  
  fig4.update_layout(title = 'Atendimento às demandas quanto ao prazo', xaxis_title = "Prazo para atendimento", yaxis_title = "Quantidade de demandas")
  st.plotly_chart(fig4, use_container_width = True)


col5, col6 = st.columns(2)

with col5:
  del_acordao = df.query('Ato == "Ciência" or Ato == "Determinação" or Ato == "Recomendação" or Ato == "Alerta"')
  filtro_del = del_acordao['Ato'].value_counts()
  fig5 = px.bar(filtro_del, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig5.update_layout(title = 'Deliberações de Acórdãos TCU', xaxis_title = "Quantidade de itens", yaxis_title = "Tipo de Deliberação")
  st.plotly_chart(fig5, use_container_width = True)

with col6:
  tratamento_det = df.query('Ato == "Determinação"')
  tratamento_det['Ato'].value_counts()
  filtro_tto_det = tratamento_det['tratamento'].value_counts()
  fig6 = px.bar(filtro_tto_det, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig6.update_layout(title = 'Situação das Determinações envolvendo o MPO', xaxis_title = "Providências", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig6, use_container_width = True)

col7, col8 = st.columns(2)

with col7:
  tratamento_rec = df.query('Ato == "Recomendação"')
  tratamento_rec['Ato'].value_counts()
  filtro_tto_rec = tratamento_rec['tratamento'].value_counts()
  fig7 = px.bar(filtro_tto_rec, text_auto = True, color_discrete_sequence=['#2237FF'])
  fig7.update_layout(title = 'Situação das Recomendações envolvendo o MPO', xaxis_title = "Providências", yaxis_title = "Quantidade de itens")
  st.plotly_chart(fig7, use_container_width = True)
     
  with col8:
     fig8 = px.bar(df2, x = 'ano_acordao', y = 'valor_ato', color = 'Ato')  
     fig8.update_layout(title = 'Deliberações do TCU respondidas pelo MPO desde o início da gestão', xaxis_title = "Ano da deliberação", yaxis_title = "Quantidade de itens")
     st.plotly_chart(fig8, use_container_width = True)
  

