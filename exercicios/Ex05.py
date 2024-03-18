#  Programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

from Ex04 import validador_codigo

codigo = input("Insira seu código: ")
validador_codigo(codigo)