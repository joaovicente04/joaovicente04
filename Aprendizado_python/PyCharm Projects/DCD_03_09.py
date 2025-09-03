# Funções
def saudacao():
    print("Salve!")

saudacao()

#Funcão com argumento
def boasvindas (nome,sobrenome):
    print("Bem vindo",nome,sobrenome)
boasvindas("João","Vicente")

def msg (mensagem = "Olá, tudo bem?"):
    print(mensagem)
msg("Bom dia!")
msg()

def pi ():
    return 3.141592653589793
print(f"O Valor de Pi é: {pi()}")

def soma (A=0, B=0):
    C = A + B
    print(f"A soma de {A} + {B} = {C}")
soma(23,65)
soma(23)
soma()

import random

def jogar_dados(lados):
    resultado = random.randint(1,lados)
    return resultado

entrada = int(input("Digite a quantidade de lados do dado:"))
result = jogar_dados(entrada)
print(f"O resultado foi: {result}")