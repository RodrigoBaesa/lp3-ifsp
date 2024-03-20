numero = int(input("Insira seu número para calcular tabuada: "))

for x in range(10):
    print("%d x %d = %d" % (numero, x+1, numero*(x+1)))