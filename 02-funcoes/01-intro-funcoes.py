# Função
# modularizar o programa
# reuso
# manutenabilidade

# só pode acessar hora estiver entre 8 e 18h
# dentro do horário comercial
hora_atual = 12

if hora_atual >= 8 and hora_atual <= 18:
    print("Permitido o acesso")


# entrada = hora_atual
# saida se está dentro ou não do horario comercial
def dentro_horario_comercial(hora_atual):
    if hora_atual >= 8 and hora_atual <= 18:
        return True
    else:
        return False

def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18


# Declaração
# def nome_funcao():
#     corpo da funcao
#     corpo da funcao

# Função sem 
# Side effect - efeito colateral
def diga_ola(nome):
    print(f"Olá {nome}")

# Chamada
diga_ola("Marcos")

# Função com retorno
def montar_frase(nome):
    return f"Ola {nome}"

nome = "Marcos"
print(montar_frase(nome))
#envia_email(montar_frase(nome))


# Parâmetro e Argumentos
# Parâmetro referências que podem ser acessada
# dentro da função
# Argumento são os valores passados para os parâmetros
def somar(numero1, numero2):
    return numero1 + numero2

somar(10.0, 5.0)

# Escopo de varíaveis
# Variável local
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

#print(media)

# Variàvel global
total = 0.0

def soma(n1, n2, n3):
    # global total
    total = n1 + n2 + n3
    return total

print(total)
soma(1, 3, 5)
print(total)

# Parâmetros com valor padrão (default)
def boas_vindas(nome, mensagem="Bom dia"):
    return f"{mensagem}, {nome}"

print(boas_vindas("Mrcos", "Bom dia"))
print(boas_vindas("Marilene", "Boa tarde"))
print(boas_vindas("Maria"))

# Argumentos nomeados
print(boas_vindas(nome="Maria"))

# Docstrings
def somar(n1, n2):
    '''
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: soma dois numeros
    '''
    return n1 + n2

# Funções built-in
# print, type, len, sum, max, min, input
# ver 