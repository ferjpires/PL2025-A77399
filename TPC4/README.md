# 📌 TPC4 - Analisador Léxico para Linguagem de Query

## 📅 Data
05/03/2025

## 👤 Autor
- **Nome:** Fernando Pires
- **Número de Aluno:** A77399
<img src="../fernandopires.jpg" alt="Fernando Pires" width="200" />

## 📖 Resumo
Neste trabalho, foi desenvolvido um analisador léxico utilizando a biblioteca ply.lex em Python. O objetivo foi construir um tokenizer capaz de processar queries semelhantes às utilizadas em linguagens como SPARQL, identificando corretamente palavras-chave, identificadores, strings, números e símbolos.

A implementação seguiu a seguinte estrutura:

**Palavras-chave:** As palavras reservadas como *SELECT*, *WHERE* e *LIMIT* foram armazenadas num dicionário, permitindo que o analisador as reconheça corretamente.

**Identificadores:** Foram configurados para suportar nomes de entidades, incluindo prefixos como dbo:MusicalArtist e foaf:name.

**Strings:** Implementada uma regra de reconhecimento para capturar texto entre aspas duplas, incluindo a possibilidade de tags de idioma opcionais, como "Chuck Berry"@en.

**Números:** Tratados como sequências numéricas e convertidos automaticamente para inteiros, úteis para comandos como LIMIT 1000.

**Símbolos Especiais:** Elementos como . (ponto), ? (interrogação), {, } são identificados como tokens individuais.

**Comentários:** Qualquer linha iniciada com # é ignorada pelo analisador.

**Gestão de Linhas:** A contagem de linhas é atualizada para facilitar a depuração e indicar possíveis erros.

## 📂 Resultados
O código do analisador encontra-se no seguinte ficheiro:

tpc4.py - [Ficheiro com o código]
