x = 0
y = 0
z = 0

while True:    
    voto = input("Digite [X] para votar no candidato X\nDigite [Y] para votar no candidato Y\nDigite [Z] para votar no candidato Z\n\nDigite [1] para sair.\n \n")
    if voto == "1":
        break
    if voto == "X" or voto == "x":
        x += 1
    if voto == "Y" or voto == "y":
        y += 1
    if voto == "Z" or voto == "z":
        z += 1
            
print("O candidato X teve {x} votos!", x)
print("O candidato Y teve {y} votos!", y)
print("O candidato Z teve {z} votos!", z)