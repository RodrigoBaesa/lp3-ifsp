# if, if/else, if,elif,else, ternario, match

# if
# if condicao:
#    corpo
#    corpo
#    corpo

idade = 20
if idade >= 18:
    print("Maior de idade")
    print("Acabou o programa")

# if/else
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("Agora acabou")

# criança (0-12), adolescente(13-17), adulto(18-59) ou idoso (60+)
if idade <= 12:
    print("C")
elif idade <=17:
    print("Adol")
elif idade<= 59:
    print("Adul")
else:
    print("Idoso")

# if aninhado (evitar)
email = "cellbits@email.com"
senha = "lore1234"

if email == "cellbits@email.com":
    if senha == "lore1234":
        print("Acesso liberado")
    else:
        print("email ou senha incorretos")
else:
    print("Email ou senha incorretos")

if email == "cellbits@email.com" and senha == "lore1234":
    print("Acesso Liberado")
else:
    print("Email ou senha incorretos")

# condição complexa no if
# permitir a entrada se:
# o usuário não estiver bloqueado E
# o usuário for um funcionário E
# o  hora atual entre 08 e 18
# OU
# o usuário é admin

usuario_bloqueado = False
usuario_funcionario = True
hora_atual = 19
usuario_admin = False
if not (usuario_bloqueado and usuario_funcionario and hora_atual >= 8 and hora_atual <=18) and usuario_admin:
    print("Liberado")
else:
    print("Não liberado")

horario_comercial = hora_atual >=8 and hora_atual <= 18
usuario_ativo = usuario_funcionario and not usuario_bloqueado
liberado = (usuario_ativo and horario_comercial) or usuario_admin

if liberado:
    print("liberado")
else:
    print("Não liberado")

# entrada: hora_atual
# saida: hora_atual está dentro do horário comercial (bool)
def dentro_horario_comercial(hora_atual):
    return hora_atual >=8 and hora_atual <= 18

# operador ternario
if idade >= 18:
    status = "maior"
else:
    status = "menor"

status = "maior" if idade >= 18 else "menor"

# usuario passa o dia (int)
# devolve string nome
# 1 - Domingo, 2 - Segunda .....7 - Sábado
dia = 4

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}

if dia in dias:
    print(dias[dia])

# match
# python 
# "switch case" mais poderoso

dia = 2
match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")

match dia:
    case 1 | 7:
        print("Fim de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")
    case _:
        print("Inválido")