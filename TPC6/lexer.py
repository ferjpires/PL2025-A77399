import ply.lex as lex

tokens = (
    'NUM',
    'PLUS', 'MINUS',
    'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    raise SyntaxError(f"Carácter inválido: {t.value[0]}")

lexer = lex.lex()
