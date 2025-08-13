import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")  # opcional: tela larga

st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações brasileiras ao longo dos anos
""")

@st.cache_data
def carregar_dados(empresas):
    dados_acao = yf.download(empresas, start='2015-01-01', end='2024-07-01')
    # Quando vários tickers são baixados, o 'Close' vira um subnível
    precos_acao = dados_acao["Close"]  
    return precos_acao

acoes = ["ITUB4.SA", "BBAS3.SA", "VALE3.SA", "ABEV3.SA", "MGLU3.SA", "PETR4.SA", "GGBR4.SA"]
dados = carregar_dados(acoes)

lista_acoes = st.multiselect(
    "Escolha as ações para exibir no gráfico",
    list(dados.columns),
    default=acoes[:3]
)

if lista_acoes:
    st.line_chart(dados[lista_acoes])
else:
    st.warning("Selecione pelo menos uma ação para exibir.")
