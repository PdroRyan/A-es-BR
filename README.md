# Preço de Ações
Este projeto é um aplicativo web interativo desenvolvido com Streamlit e yfinance para visualizar a evolução do preço de ações brasileiras ao longo dos anos.

🚀 Funcionalidades
Busca automática de dados históricos de ações usando o Yahoo Finance.

Seleção dinâmica de múltiplas ações para visualização.

Gráfico interativo de preços de fechamento.

Cache de dados para evitar requisições repetidas e acelerar a aplicação.

🖼️ Exemplo de Uso

📦 Requisitos
Antes de rodar o projeto, instale as dependências:
pip install -r requirements.txt
requirements.txt
nginx
streamlit
yfinance
pandas
▶️ Como Executar

Instale as dependências:
pip install -r requirements.txtExecute o Streamlit:

streamlit run main.py
Acesse no navegador:
http://localhost:8501
📂 Estrutura do Projeto
📁 streamlit-preco-acoes
 ├── main.py            # Código principal do app
 ├── requirements.txt   # Dependências do projeto
 └── README.md          # Documentação
📜 Código Principal (main.py)
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")

st.write("""
O gráfico abaixo representa a evolução do preço das ações brasileiras ao longo dos anos
""")

@st.cache_data
def carregar_dados(empresas):
    dados_acao = yf.download(empresas, start='2015-01-01', end='2024-07-01')
    return dados_acao["Close"]

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
📌 Observações
É necessário estar conectado à internet para que o yfinance baixe os dados.

O cache evita que a API seja chamada várias vezes, economizando tempo e recursos.

Caso queira mudar o período, altere os parâmetros start e end na função carregar_dados.

<img width="1836" height="833" alt="acoes" src="https://github.com/user-attachments/assets/5072d8e0-ebad-4bc9-b42e-1e7e5746bcf0" />
