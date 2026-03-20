import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Impacto Ofensivo", layout="wide")

st.title("Impacto Ofensivo dos Jogadores - 2025/2026")
st.success("Dashboard desenvolvido por Victor Koss")

# =========================
# CARREGAR DADOS
# =========================
@st.cache_data
def carregar_dados():
    df = pd.read_csv(r'C:\Python\players_data-2025_2026.csv')
    df = df.drop_duplicates()
    df = df.fillna(0)
    df = df[df['MP'] > 0]

    # métricas personalizadas
    df['Participacao'] = df['Gls'] + df['Ast']
    df['Impacto_Ofensivo'] = (df['Gls'] * 1.2) + df['Ast']
    df['Impacto_por_jogo'] = df['Impacto_Ofensivo'] / df['MP']

    return df

df = carregar_dados()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Filtros de Análise")

posicoes = st.sidebar.multiselect(
    "Escolha a posição:",
    options=df['Pos'].unique(),
    default=df['Pos'].unique()
)

df_filtrado = df[df['Pos'].isin(posicoes)]

# =========================
# Análise
# =========================
st.markdown("### Análise")
st.write("Jogadores com menos jogos tendem a ter maior impacto por partida.")

# =========================
# RANKING PRINCIPAL
# =========================
st.subheader("Ranking por Impacto Ofensivo")

top10 = df_filtrado.sort_values(by='Impacto_Ofensivo', ascending=False).head(10)

st.dataframe(top10[['Player', 'Pos', 'Gls', 'Ast', 'Impacto_Ofensivo']])

fig, ax = plt.subplots()
sns.barplot(x='Impacto_Ofensivo', y='Player', data=top10, ax=ax)
st.pyplot(fig)

# =========================
# IMPACTO POR JOGO
# =========================
st.subheader("Jogadores Mais Impactantes por Jogo")

top_impacto = df_filtrado.sort_values(by='Impacto_por_jogo', ascending=False).head(10)

st.dataframe(top_impacto[['Player', 'MP', 'Impacto_por_jogo']])

fig2, ax2 = plt.subplots()
sns.barplot(x='Impacto_por_jogo', y='Player', data=top_impacto, ax=ax2)
st.pyplot(fig2)

# =========================
# COMPARAÇÃO
# =========================
st.subheader("Comparação de Jogadores")

jogadores = df['Player'].unique()

j1 = st.selectbox("Jogador 1", jogadores)
j2 = st.selectbox("Jogador 2", jogadores)

comp = df[df['Player'].isin([j1, j2])]

st.dataframe(comp[['Player', 'Gls', 'Ast', 'Impacto_Ofensivo', 'MP']])

fig3, ax3 = plt.subplots()
comp.set_index('Player')[['Gls', 'Ast', 'Impacto_Ofensivo']].plot(kind='bar', ax=ax3)
st.pyplot(fig3)