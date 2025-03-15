# 📌 TPC5 - Máquina de Vending

## 📅 Data
2025-03-15

## 👤 Autor
- **Nome:** Fernando Pires
- **Número de Aluno:** A77399
<img src="../fernandopires.jpg" alt="Fernando Pires" width="200" />

## 📖 Resumo
Este trabalho consiste na implementação de um simulador de máquina de vending com gestão de stock e transações utilizando a biblioteca `ply.lex` em Python. O objetivo foi desenvolver um programa capaz de processar comandos do utilizador, gerir um stock persistente, aceitar moedas como pagamento e dispensar produtos conforme apropriado.

### **Estrutura do Programa**
O programa foi estruturado da seguinte forma:
1. **Carregamento do Stock:** O stock é lido a partir de um ficheiro JSON. Se o ficheiro não existir, o stock inicializa-se vazio.
2. **Analisador Léxico:** Utiliza `ply.lex` para reconhecer comandos como `LISTAR`, `MOEDA`, `SELECIONAR` e `SAIR`.
3. **Gestão de Saldo:** Mantém registo do saldo do utilizador e das moedas inseridas.
4. **Processamento de Comandos:** Implementa regras para cada comando, atualizando o stock e o saldo de acordo com as ações do utilizador.
5. **Persistência:** Ao sair, o stock atualizado é guardado no ficheiro JSON para manter o estado entre sessões.

#### **Carregamento e Persistência do Stock**
```python
try:
    with open('stock.json', 'r') as f:
        stock = json.load(f)
except FileNotFoundError:
    stock = []
```
O stock é carregado ao iniciar o programa. Se o ficheiro não existir, inicializa-se um stock vazio.

#### **Analisador Léxico**
Defini regras para reconhecer diferentes tipos de tokens:
- Comandos (`LISTAR`, `MOEDA`, `SELECIONAR`, `SAIR`)
- Código de produto (`CODIGO`)
- Valores de moeda (`VALOR`)
- Separadores (`VIRGULA`, `PONTO`)

#### **Processamento de Comandos**
A função `processar_comando` interpreta a entrada do utilizador e executa as ações correspondentes:
- **LISTAR:** Exibe o stock disponível.
- **MOEDA:** Regista as moedas inseridas e atualiza o saldo.
- **SELECIONAR:** Verifica se o produto existe e se há saldo suficiente para comprá-lo.
- **SAIR:** Calcula o troco a devolver e guarda o estado do stock.

#### **Cálculo de Troco**
A função `calcular_troco` determina as moedas a devolver, garantindo o menor número possível de moedas através de um algoritmo guloso.

## 📂 Resultados
Os ficheiros principais do projeto são:
- [`tpc5.py`](tpc5.py) - [Código fonte]
- [`stock.json`](stock.json) - [Ficheiro de persistência do stock]

