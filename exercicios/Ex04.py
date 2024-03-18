import re

def validador_codigo(codigo):
    validacao = "^BR\d{4}X$"
    if re.match(validacao, codigo) and codigo != "BR0000X":
            print("Seu código identificador é válido!")
    else:
        print("Seu código identificador é inválido")