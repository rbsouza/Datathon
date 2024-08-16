import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Função para aplicar encoding nas variáveis categóricas
def encode_categorical(df):
    le = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = le.fit_transform(df[column])
    return df

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
st.pyplot(plt, use_container_width=True)

# Boxplot
st.write(f'Boxplot de {variable}')
fig, ax = plt.subplots()
sns.boxplot(x=df[variable], ax=ax)
st.pyplot(fig, use_container_width=True)

# Aplicar encoding nas variáveis categóricas
df_encoded = encode_categorical(df)

# Correlação
st.subheader('Matriz de Correlação')
fig, ax = plt.subplots()
sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig, use_container_width=True)