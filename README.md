##⚽ Fut Stats

Impacto Ofensivo dos Jogadores na Temporada 2025|2026
Desenvolvido por Victor Yuri

Fut Stats é uma aplicação interativa que permite analisar o desempenho ofensivo de jogadores de futebol, destacando gols, assistências e impacto por partida, utilizando Streamlit, Pandas, Matplotlib e Seaborn.

##🏆 Funcionalidades
1. Carregamento de dados

Lê arquivos CSV com estatísticas dos jogadores.

Remove duplicatas, preenche valores nulos e filtra jogadores que não participaram de partidas.

2. Métricas personalizadas

Participação: soma de gols e assistências (Gls + Ast).

Impacto Ofensivo: combinação ponderada de gols e assistências (Gls * 1.2 + Ast).

Impacto por Jogo: impacto ofensivo dividido pelo número de partidas (Impacto_Ofensivo / MP).

3. Filtros interativos

Seleção de posições específicas dos jogadores para análise.

4. Classificação de jogadores

Visualiza os Top 10 jogadores por impacto ofensivo.

Exibe tabela e gráfico de barras.

5. Impacto por jogo

Mostra os jogadores mais impactantes por partida.

Visualização em tabela e gráfico de barras.

6. Comparação entre jogadores

Seleção de dois jogadores para comparar gols, assistências, impacto ofensivo e partidas jogadas.

Gráfico de barras comparativo para melhor visualização.

🚀 Como usar
Pré-requisitos

Python 3.8 ou superior

Instalar as bibliotecas necessárias:

pip install pandas streamlit matplotlib seaborn

Executar a aplicação

No terminal, dentro da pasta do projeto:

streamlit run fut_stats.py

A interface abrirá automaticamente no navegador.

Interagir com os dados

Use a barra lateral para filtrar posições.

Explore tabelas e gráficos para visualizar os jogadores mais impactantes.

Compare jogadores específicos usando o menu de seleção.

📂 Estrutura do Projeto

├─ fut_stats.py                 # Código principal da aplicação Streamlit
├─ players_data-2025_2026.csv   # Dados dos jogadores


📬 Contato

Desenvolvido por Victor Yuri

LinkedIn: https://www.linkedin.com/in/victor-yuri-65147136a/




