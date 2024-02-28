# Identificadores
# Letra, números e ...
# Não pode ser palavras reservada: if, None, True, False
# Case sensitive
nome = "Pedro"
Nome = "Pedro"

# Variáveis
# Tudo em minúsculo
# Separador ...
# snake_case
idade = 20
pessoa_fisica = "Marcio"
pessoa_juridica = "Paula LTDA"
imposto_renda = 2200.45

# É o tipo?
# Java
# String nome = "Pedro"
# int idade = 20
# No Python temos inteferência de tipo
# O tipo será definido com base no valor
idade = 20 # int
nome = "Pedro" # str

# Constantes
# Não existe constante no Python
# Convenção: nome em maiúsculo
PI = 3.14

'''
Comentário
de múltiplas linhas
'''

# docstring (comentários de documentação)
# documentar classe, módulos, funções, ...

def somar(numero1, numero2):
    '''
    Função que soma dois números
    :param numero1: primeiro numero
    :param numero2: segundo número
    :return a soma dos dois números
    '''
    return numero1 + numero2