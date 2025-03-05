import ply.lex as lex

# Palavras reservadas
reserved = {
    'select': 'SELECT',
    'where': 'WHERE',
    'limit': 'LIMIT',
}

# Lista de tokens
tokens = [
    'IDENTIFIER', 'STRING', 'NUMBER',
    'DOT', 'QMARK', 'LBRACE', 'RBRACE',
] + list(reserved.values())

# Expressões regulares para tokens simples
t_DOT = r'\.'
t_QMARK = r'\?'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Expressão para identificadores
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_:]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')  # Verifica palavras reservadas
    return t

# Expressão para strings
def t_STRING(t):
    r'"[^"]*"(?:@[a-zA-Z]+)?'
    return t

# Expressão para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espaços e tabs
t_ignore = ' \t'

# Comentários iniciados por #
def t_COMMENT(t):
    r'\#.*'
    pass

# Tratamento de erros
def t_error(t):
    print(f"Caráter ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()

# Exemplo de input
data = '''
# DBPedia: obras de Chuck Berry
select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000
'''

lexer.input(data)

# Imprimir os tokens gerados
print("Tokens gerados:")
for tok in lexer:
    print(tok)
