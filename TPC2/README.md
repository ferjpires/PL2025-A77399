# 📌 TPC2 - Análise de um dataset de obras musicais

## 📅 Data
21/02/2025

## 👤 Autor
- **Nome:** Fernando Pires
- **Número de Aluno:** A77399
<img src="../fernandopires.jpg" alt="Fernando Pires" width="200" />

## 📚 Resumo
Para resolver o problema proposto, foi desenvolvido um script que processa um ficheiro CSV de obras musicais, normalizando-o e extraindo informações relevantes. O código está organizado da seguinte forma:

- **Normalização do CSV:** Como as descrições das obras podem conter quebras de linha que dificultam a leitura, é aplicado um processo de normalização, substituindo quebras de linha por espaços para garantir que cada entrada do CSV fique em uma única linha.
- **Leitura do CSV:** O ficheiro é lido linha a linha, e os dados são armazenados em dicionários para facilitar a manipulação posterior.
- **Ordenação de compositores:** Os compositores presentes no dataset são extraídos e ordenados alfabeticamente.
- **Contagem de obras por período:** As obras são categorizadas por período, e é calculada a quantidade de obras em cada um.
- **Associação de títulos por período:** Os títulos das obras são agrupados por período e ordenados alfabeticamente.

### ⚙️ Implementação das alíneas:

- **Alínea 1:** Ordenação dos compositores de forma alfabética. Os nomes são extraídos diretamente do CSV, armazenados num conjunto para evitar duplicados e ordenados antes de serem apresentados.
- **Alínea 2:** Contagem das obras por período. Para cada linha do CSV, o período da obra é identificado e contabilizado num dicionário.
- **Alínea 3:** Associação dos títulos das obras aos seus respetivos períodos. A lista de títulos para cada período é ordenada alfabeticamente antes da impressão.

## 📂 Resultados
Os seguintes ficheiros foram produzidos:
- [`processar_obras.py`](processar_obras.py) - [Script principal para processamento dos dados]
- [`obras.csv`](obras.csv) - [Ficheiro original de dados]
- [`obras_normalizado.csv`](obras_normalizado.csv) - [Ficheiro CSV normalizado]

---

