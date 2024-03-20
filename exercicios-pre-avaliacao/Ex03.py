frase = str(input("Insira uma frase ou palavra: "))

def contar_vogal(char):
    vogal = "aeiouAEIOU"
    return char in vogal

def contar_consoante(char):
    return char.isalpha() and not contar_vogal(char)

qnt_vogal = 0
qnt_consoante = 0

for char in frase:
    if contar_vogal(char):
        qnt_vogal += 1
    elif contar_consoante(char):
        qnt_consoante += 1
        
print("Na sua frase contém %d vogais " % qnt_vogal)
print("Na sua frase contém %d consoantes" % qnt_consoante)