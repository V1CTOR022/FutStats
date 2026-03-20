# ⚽ Fut Stats  

**Impacto Ofensivo dos Jogadores na Temporada 2025|2026**  
Desenvolvido por **Victor Yuri**  

Fut Stats é uma aplicação interativa que permite analisar o desempenho ofensivo de jogadores de futebol, destacando gols, assistências e impacto por partida, utilizando **Streamlit**, **Pandas**, **Matplotlib** e **Seaborn**.  

---

## 🏆 Funcionalidades

### 1. Carregamento de dados
- Lê arquivos CSV com estatísticas dos jogadores.  
- Remove duplicatas, preenche valores nulos e filtra jogadores que não participaram de partidas.  

---

### 2. Métricas personalizadas
- **Participação**: soma de gols e assistências (`Gls + Ast`).  
- **Impacto Ofensivo**: combinação ponderada de gols e assistências (`Gls * 1.2 + Ast`).  
- **Impacto por Jogo**: impacto ofensivo dividido pelo número de partidas (`Impacto_Ofensivo / MP`).  

---

### 3. Filtros interativos
- Permite selecionar posições específicas dos jogadores para análise.  

---

### 4. Classificação de jogadores
- Visualiza os **Top 10 jogadores** por impacto ofensivo.  
- Exibe tabela e gráfico de barras.  

---

### 5. Impacto por jogo
- Mostra os jogadores mais impactantes por partida.  
- Visualização em tabela e gráfico de barras.  

---

### 6. Comparação entre jogadores
- Seleção de **dois jogadores** para comparar gols, assistências, impacto ofensivo e partidas jogadas.  
- Gráfico de barras comparativo para melhor visualização.  

---

## 🚀 Como usar

### Pré-requisitos
- Python 3.8 ou superior  
- Instalar as bibliotecas necessárias:  
```bash
pip install pandas streamlit matplotlib seaborn
