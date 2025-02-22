import re

def markdown_para_html(md_texto):
    """Converte um texto em Markdown para HTML."""
    linhas = md_texto.split('\n')
    html_saida = []
    dentro_lista = False

    for linha in linhas:
        linha = linha.strip()

        # Cabeçalhos
        if re.match(r'^### (.+)', linha):
            html_saida.append(f"<h3>{linha[4:]}</h3>")
            continue
        elif re.match(r'^## (.+)', linha):
            html_saida.append(f"<h2>{linha[3:]}</h2>")
            continue
        elif re.match(r'^# (.+)', linha):
            html_saida.append(f"<h1>{linha[2:]}</h1>")
            continue

        # Bold
        linha = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', linha)
        
        # Itálico
        linha = re.sub(r'\*(.*?)\*', r'<i>\1</i>', linha)
        
        # Listas numeradas
        if re.match(r'^\d+\.\s+(.+)', linha):
            if not dentro_lista:
                html_saida.append("<ol>")
                dentro_lista = True
            item = re.sub(r'^\d+\.\s+', '', linha)
            html_saida.append(f"<li>{item}</li>")
        else:
            if dentro_lista:
                html_saida.append("</ol>")
                dentro_lista = False
            
            # Imagens (deve ser tratado antes de links para evitar conflitos)
            linha = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', linha)
            
            # Links
            linha = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', linha)
            
            html_saida.append(linha)
    
    if dentro_lista:
        html_saida.append("</ol>")
    
    return '\n'.join(html_saida)

# Teste
teste_md = """# Título Principal
## Subtítulo
### Cabeçalho Menor

Este é um **texto em negrito** e este é um *texto em itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Veja esta imagem: ![imagem dum coelho](http://www.coellho.com)
"""

print(markdown_para_html(teste_md))
