import re

def formatar_csv(ficheiro_entrada, ficheiro_saida):
    with open(ficheiro_entrada, 'r', encoding='utf-8') as entrada, \
         open(ficheiro_saida, 'w', encoding='utf-8') as saida:
        conteudo = entrada.read()
        normalizado = re.sub(r'\n\s+', ' ', conteudo)
        saida.write(normalizado)

def ler_csv(ficheiro):
    with open(ficheiro, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    cabecalho = linhas[0].strip().split(';')
    dados = []
    for linha in linhas[1:]:
        valores = linha.strip().split(';')
        if len(valores) == len(cabecalho):
            dados.append(dict(zip(cabecalho, valores)))
    
    return dados

def ordenar_compositores(dados):
    compositores = set(dado['compositor'] for dado in dados if 'compositor' in dado)
    return sorted(compositores)

def contar_obras_por_periodo(dados):
    periodos = {}
    for dado in dados:
        periodo = dado.get('periodo', 'Desconhecido')
        periodos[periodo] = periodos.get(periodo, 0) + 1
    return periodos

def listar_titulos_por_periodo(dados):
    periodos = {}
    for dado in dados:
        periodo = dado.get('periodo', 'Desconhecido')
        titulo = dado.get('nome', 'Sem título')
        periodos.setdefault(periodo, []).append(titulo)
    for periodo in periodos:
        periodos[periodo].sort()
    return periodos

def main():
    ficheiro_entrada = 'obras.csv'
    ficheiro_formatado = 'obras_normalizado.csv'
    
    formatar_csv(ficheiro_entrada, ficheiro_formatado)

    dados = ler_csv(ficheiro_formatado)
    
    compositores_ordenados = ordenar_compositores(dados)
    obras_por_periodo = contar_obras_por_periodo(dados)
    titulos_por_periodo = listar_titulos_por_periodo(dados)
    
    print("Compositores ordenados:")
    for compositor in compositores_ordenados:
        print(compositor)
    
    print("\nQuantidade de obras por período:")
    for periodo, quantidade in obras_por_periodo.items():
        print(f"{periodo}: {quantidade}")
    
    print("\nTítulos por período:")
    for periodo, titulos in titulos_por_periodo.items():
        print(f"{periodo}: {len(titulos)} obras")
        for titulo in titulos:
            print(f"    {titulo}")

if __name__ == '__main__':
    main()
