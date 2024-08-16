import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar dados de um URL
@st.cache_data
def load_data(url):
    return pd.read_csv(url, encoding='utf-8-sig')

# URLs diretos para os arquivos CSV no GitHub
url_2020 = 'https://raw.githubusercontent.com/rbsouza/Datathon/main/data/arquivo_2020.csv'
url_2021 = 'https://raw.githubusercontent.com/rbsouza/Datathon/main/data/arquivo_2021.csv'
url_2022 = 'https://raw.githubusercontent.com/rbsouza/Datathon/main/data/arquivo_2022.csv'

# Carregar os dados
df_2020 = load_data(url_2020)
df_2021 = load_data(url_2021)
df_2022 = load_data(url_2022)

# Título do dashboard
st.title('Análise Exploratória de Dados - Datathon')

# Seleção do ano
year = st.selectbox('Selecione o ano', ['2020', '2021', '2022'])

# Selecionar o dataframe com base no ano escolhido
if year == '2020':
    df = df_2020
elif year == '2021':
    df = df_2021
else:
    df = df_2022

# Mostrar os dados
st.subheader(f'Dados do ano {year}')
st.write(df.head())

# Análise descritiva
st.subheader('Análise Descritiva')
st.write(df.describe())

# Gráficos
st.subheader('Distribuição das Variáveis')

# Seleção da variável para o gráfico
variable = st.selectbox('Selecione a variável', df.columns)

# Exibir gráfico da variável selecionada
st.subheader(f'Distribuição da variável {variable}')
plt.figure(figsize=(10, 6))
sns.histplot(df[variable], kde=True)
st.pyplot(plt)
