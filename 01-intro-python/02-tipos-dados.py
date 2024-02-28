# 1. Números

# int
idade = 20

# float
altura = 1.6

# complex
# cálculos com números complexos
numero_complexo = 1 + 2j

# 2. Boolean
verdade = True
mentira = False

# 3. Sequências
# str, list, tuple, set, dict

# str
# conjunto de caracteres
nome = "João da Silva"
nome = "Maria da Silva"

# str de múltiplas lihas
frase = """
Olá mundo"
Parabéns Amigo
"""

# Interpolação de str
nome = "Maria"
idade = 78
mensagem = f"{nome}NOME é uma pessoa legal! Ela tem {idade} anos"

# char
# não existe
# usar str de tamanho 1
letra = "A"

# Como acessar os caracteres de uma str?
nome = "Silvio Santos"
print(nome[2])

# Métodos de str
print(nome.upper())
print(nome.capitalize())
print(nome)

# list
# lista de valores

habilidades = ["Python", "Java", "Javascript"]
print(habilidades[1])

for habilidade in habilidades:
    print("Teste")
    print(habilidades)

# Adiciona no final da lista
habilidades.append("html")

# Adiciona em uma posição
habilidades.insert(1, "css") # "python", "css", "java", "javascript", "html"

# Remover
habilidades.remove("css")

# tuple
# "lista" de valores
# Não pode ser alterada
# Sim, não, talvez
opcoes = ("sim", "não", "talvez")
raca_rpg = ("humano", "elfo", "orc")

def estatistica_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    return maior, menor, media

notas = [10.0, 3.5, 7.8]
estatistica = estatistica_notas(notas)
print(estatistica)

# Desempacotar como tupla
maior, menor, media = estatistica_notas(notas)
print(maior, menor, media)

# set
# Conjunto de valores
# Não é indexado
# Permite elementos duplicados
habilidades = {"java", "python"}
habilidades.add("java")
print(habilidades)

for habilidades in habilidades:
    print(habilidade)

# dict
# palavra -> definicao
# chave -> valor
# key -> value

nome = "Silvio"
idade = 89
patrimonio = 2000000
altura = 1.7

pessoa = {
    "nome": "Silvio",
    "idade": 89,
    "patrimonio": 2000000,
    "altura": 1.7
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["patrimonio"])
print(pessoa["altura"])

# None
# Variáveis que serão inicializadas em tempo de execução
# retorno de função
# parametros de função
nulo = None