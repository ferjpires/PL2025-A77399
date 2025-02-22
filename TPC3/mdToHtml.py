import re

def markdown_para_html(md_texto):
    linhas = md_texto.split('\n')
    html_saida = []
    dentro_lista = False

    for linha in linhas:
        linha = linha.strip()

        # Cabeçalhos
        if re.match(r'^### (.+)', linha):
            html_saida.append(f"<h3>{linha[4:]}</h3>")
        elif re.match(r'^## (.+)', linha):
            html_saida.append(f"<h2>{linha[3:]}</h2>")
        elif re.match(r'^# (.+)', linha):
            html_saida.append(f"<h1>{linha[2:]}</h1>")

        # Bold
        elif re.search(r'\*\*(.*?)\*\*', linha):
            linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha)
            html_saida.append(linha)

        # Itálico
        elif re.search(r'\*(.*?)\*', linha):
            linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)
            html_saida.append(linha)

        # Listas numeradas
        elif re.match(r'^\d+\.\s+(.+)', linha):
            if not dentro_lista:
                html_saida.append("<ol>")
                dentro_lista = True
            item = re.sub(r'^\d+\.\s+', '', linha)
            html_saida.append(f"<li>{item}</li>")
        else:
            if dentro_lista:
                html_saida.append("</ol>")
                dentro_lista = False
            
            # Links
            linha = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', linha)
            
            # Imagens
            linha = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', linha)
            
            html_saida.append(linha)
    
    if dentro_lista:
        html_saida.append("</ol>")
    
    return '\n'.join(html_saida)

# Teste
teste_md = """# Exemplo
## Subtítulo
### Terceiro nível

Este é um **exemplo** de *Markdown*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Veja esta imagem: ![imagem dum coelho](http://www.coellho.com)
"""

print(markdown_para_html(teste_md))
