import ply.yacc as yacc
from lexer import tokens

# Definição da precedência e associatividade dos operadores
precedence = (
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO'),
)

# Regra de produção
def p_programa(p):
    '''
    programa : expressao
    '''
    p[0] = p[1]

# Regra para expressões aritméticas
def p_expressao(p):
    '''
    expressao : expressao SOMA expressao
              | expressao SUBTRACAO expressao
              | expressao MULTIPLICACAO expressao
              | expressao DIVISAO expressao
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

# Regra para fatores numéricos
def p_expressao_numero(p):
    '''
    expressao : NUMERO
    '''
    p[0] = p[1]

# Regra para fatores dentro de parênteses
def p_expressao_parenteses(p):
    '''
    expressao : ABRE_PARENTESES expressao FECHA_PARENTESES
    '''
    p[0] = p[2]

# Função de erro de sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe: token '{p.value}' inválido na posição {p.lexpos}")
    else:
        print("Erro de sintaxe: fim inesperado do input")

# Construir o parser
parser = yacc.yacc()

# Exemplo de uso
data = '3 + 4 * 2'
result = parser.parse(data)
print(result)
