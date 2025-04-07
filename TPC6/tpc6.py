from parser import Parser

def testar(expressao):
    try:
        parser = Parser(expressao)
        resultado = parser.parse()
        print(f"{expressao} = {resultado}")
    except SyntaxError as e:
        print(f"Erro ao analisar '{expressao}': {e}")

# Testes fornecidos
expressoes = [
    "2+3",
    "67-(2+3*4)",
    "(9-2)*(13-4)",
    "3+4*2/(1-5)",       # Deve ser 3 + (4*2)/(-4) = 3 - 2 = 1
    "((2+3)*4)-5"        # Deve ser (5*4) - 5 = 15
]

for expr in expressoes:
    testar(expr)
