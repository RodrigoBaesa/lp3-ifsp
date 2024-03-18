comprimento = float(input("Insira o comprimento de um aquário: "))
altura = float(input("Insira a altura de um aquário: "))
largura = float(input("Insira a largura de um aquário: "))
temp_desejada = float(input("Insira a temperatura desejada: "))
temp_ambiente = float(input("Insira a temperatura ambiente: "))

def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_termostato(comprimento, altura, largura, temp_desejada, temp_ambiente):
    volume = calcular_volume(comprimento, altura, largura)
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def calcular_filtragem(comprimento, altura, largura):
    volume = calcular_volume(comprimento, altura, largura)
    return volume * 2.5

volume = calcular_volume(comprimento, altura, largura)
potencia = calcular_termostato(comprimento, altura, largura, temp_desejada, temp_ambiente)
filtragem = calcular_filtragem(comprimento, altura, largura)

print("\nVolume: ", volume)
print("Potencia do termostato: ", potencia)
print("Filtragem por hora: ", filtragem)