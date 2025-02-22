# 📌 TPC3 - Conversor de Markdown para HTML

## 📅 Data
22/02/2025

## 👤 Autor
- **Nome:** Fernando Pires
- **Número de Aluno:** A77399
<img src="../fernandopires.jpg" alt="Fernando Pires" width="200" />

## 📚 Resumo
Este tpc consiste na implementação de um conversor de Markdown para HTML em Python, suportando os elementos definidos na "Basic Syntax" da Cheat Sheet de Markdown. O conversor processa texto em Markdown e gera o equivalente em HTML.

### ⚙️ Funcionalidades Implementadas:
- **Cabeçalhos** (`#`, `##`, `###`) → Convertidos para `<h1>`, `<h2>`, `<h3>`.
- **Negrito** (`**texto**`) → Convertido para `<b>texto</b>`.
- **Itálico** (`*texto*`) → Convertido para `<i>texto</i>`.
- **Listas numeradas** (`1. item`) → Convertidas para `<ol><li>item</li></ol>`.
- **Imagens** (`![alt](URL)`) → Convertidas para `<img src="URL" alt="alt"/>`.
- **Links** (`[texto](URL)`) → Convertidos para `<a href="URL">texto</a>`.

## 📂 Resultados
Os seguintes ficheiros foram produzidos:
- [`mdToHtml.py`](mdToHtml.py) - [Script principal para a conversão de Markdown para HTML]

## 📊 Exemplo de Entrada e Saída
### Entrada (Markdown):
```
# Título Principal
## Subtítulo
### Cabeçalho Menor

Este é um **texto em negrito** e este é um *texto em itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Veja esta imagem: ![imagem dum coelho](http://www.coellho.com)
```

### Saída (HTML):
```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
<h3>Cabeçalho Menor</h3>

Este é um <b>texto em negrito</b> e este é um <i>texto em itálico</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>.

Veja esta imagem: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```


