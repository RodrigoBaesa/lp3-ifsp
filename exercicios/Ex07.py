peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em metros: "))

def calcular_imc(altura, peso):
    return peso / (altura * altura)

def medir_classificacao(altura, peso):
    imc = calcular_imc(altura, peso)

    if imc < 18.5:
        return "Baixo peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Excesso de peso"
    elif imc < 34.9:
        return "Obesidade de Classe 1"
    elif imc < 39.9:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def peso_ideal(altura, peso):
    imc = calcular_imc(altura, peso)
    
    if imc < 18.5:
        peso_necessario = (18.5 * altura * altura) - peso
        return f"Você precisa ganhar {peso_necessario} Kg"
    else:
        peso_necessario = (24.9 * altura * altura) - peso
        return f"Você precisa perder {peso_necessario} Kg"
    
print(peso_ideal(altura, peso))
print(medir_classificacao(altura, peso))