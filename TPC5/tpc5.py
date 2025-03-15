import ply.lex as lex
import json
import sys

try:
    with open('stock.json', 'r') as file:
        stock = json.load(file)
except FileNotFoundError:
    stock = []

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'CODIGO',
    'VALOR',
    'VIRGULA',
    'PONTO'
]

def t_LISTAR(t):
    r'LISTAR'
    return t

def t_MOEDA(t):
    r'MOEDA'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    return t

def t_SAIR(t):
    r'SAIR'
    return t

def t_CODIGO(t):
    r'[A-Z]\d\d'
    return t

def t_VALOR(t):
    r'\d+[ce]?'
    return t

t_VIRGULA = r','  
t_PONTO = r'\.'  

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"[LEXER] Símbolo não reconhecido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

saldo = 0.0
moedas_inseridas = []

def processar_comando(entrada):
    global saldo
    global moedas_inseridas

    lexer.input(entrada)
    comando = []
    while (token := lexer.token()) is not None:
        comando.append(token)
    
    if not comando:
        return
    
    if comando[0].type == 'LISTAR':
        print("cod | nome | quantidade | preço")
        print("---------------------------------")
        for produto in stock:
            print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']:.2f}€")
    elif comando[0].type == 'MOEDA':
        valores = []
        for token in comando[1:]:
            if token.type == 'VALOR':
                valor = token.value
                moeda = int(valor[:-1]) / 100 if valor.endswith('c') else int(valor[:-1]) if valor.endswith('e') else int(valor)
                valores.append(moeda)
        saldo += sum(valores)
        moedas_inseridas.extend(valores)
        print(f"maq: Saldo = {saldo:.2f}€")
    elif comando[0].type == 'SELECIONAR':
        if len(comando) < 2 or comando[1].type != 'CODIGO':
            print("maq: Comando inválido. Use SELECIONAR <código>")
            return
        codigo = comando[1].value
        produto = next((p for p in stock if p['cod'] == codigo), None)
        if not produto:
            print("maq: Produto inexistente.")
            return
        if produto['quant'] == 0:
            print("maq: Produto esgotado.")
            return
        if saldo >= produto['preco']:
            produto['quant'] -= 1
            saldo -= produto['preco']
            print(f"maq: Produto dispensado: \"{produto['nome']}\"")
            print(f"maq: Saldo = {saldo:.2f}€")
        else:
            print("maq: Saldo insuficiente para esta compra.")
            print(f"maq: Saldo = {saldo:.2f}€; Preço = {produto['preco']:.2f}€")
    elif comando[0].type == 'SAIR':
        troco = calcular_troco(saldo)
        print("maq: Retire o seu troco: ", ", ".join(troco))
        saldo = 0.0
        moedas_inseridas.clear()
        print("maq: Obrigado e até à próxima!")
        with open('stock.json', 'w') as file:
            json.dump(stock, file)
        sys.exit()
    else:
        print("maq: Comando não reconhecido.")

def calcular_troco(valor):
    moedas = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02]
    troco = []
    for moeda in moedas:
        while valor >= moeda:
            troco.append(moeda)
            valor -= moeda
    resultado = []
    contagem = {m: troco.count(m) for m in set(troco)}
    for moeda, quantidade in contagem.items():
        resultado.append(f"{quantidade}x {int(moeda) if moeda >= 1 else int(moeda * 100)}{'e' if moeda >= 1 else 'c'}")
    return resultado

def main():
    print("maq: Estado atualizado. Stock carregado." if stock else "maq: Estado atualizado. Stock não encontrado.")
    print("maq: Bem-vindo! Insira um comando.")
    while True:
        try:
            entrada = input(">> ")
            processar_comando(entrada)
        except EOFError:
            print("\nmaq: Até breve!")
            break

if __name__ == "__main__":
    main()
