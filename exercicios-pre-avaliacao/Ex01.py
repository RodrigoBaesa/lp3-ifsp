import random

numero = random.randint(1, 100)

print(numero)

while True:
    palpite = int(input("Insira seu palpite do número: "))
    if palpite == numero:
        print("Parabéns, você acertou!")
        break
    if palpite > numero:
        print("Tente novamente, o seu palpite está muito alto!")
    else:
        print("Tente novamente, o seu palpite esta muito baixo!")