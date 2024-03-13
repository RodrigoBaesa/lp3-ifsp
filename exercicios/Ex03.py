'''
Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
    Compras iguais ou superiores a R$ 500,00 - 15% de desconto

'''

valor_compra = float(input("Insira o valor da sua compra: "))

if valor_compra < 9.99:
    print(f"Sua compra não tem disconto e deu: {valor_compra}")
elif valor_compra < 99.99:
    valor_com_desconto = (valor_compra * 0.95)
    print(f"Sua compra deu: {valor_com_desconto}")
elif valor_compra < 499.99:
    valor_com_desconto = (valor_compra * 0.90)
    print(f"Sua compra deu: {valor_com_desconto}")
else:
    valor_com_desconto = (valor_compra * 0.85)
    print(f"Sua compra deu: {valor_com_desconto}")