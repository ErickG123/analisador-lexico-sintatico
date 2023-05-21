# Importação da biblioteca ply
import ply.lex as lex

# Lista de tokens
tokens = [
    'NUMERO',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
]

# Expressões regulares para os tokens
t_SOMA = r'\+'
t_SUBTRACAO = r'\-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'\/'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()

# Exemplo de uso
data = '3 + 4 * (2 - 1) / 5'
lexer.input(data)
for token in lexer:
    print(token)
