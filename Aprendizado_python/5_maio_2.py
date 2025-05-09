#Exemplo de como usar a função def
# def calcula_dobro (p_valor):
#     dobro = p_valor * 2
#     return dobro
# valor = int(input("Valor inteiro: "))
# v_retornado = calcula_dobro (valor)
# print(f"Valor retornado pela função: {v_retornado} ")

#Questão 1
# def mostra_valor(valor):
#     print(f"Parâmetro recebido: {valor} ")
# def mostra_2valores(a,b):
#     print(f"Parâmetros recebidos: {a,b}")
# if __name__ == '__main__':
#     # print("Primeira forma de fazer (sem variáveis, passa o valor direto): ")
    # mostra_valor(5)
    # mostra_valor(23.8)
    # print("Segunda forma de fazer (oom variáveis, com input)")
    # v_inteiro = int(input("Valor inteiro: "))
    # mostra_valor(v_inteiro)
    # v_real = float(input("Valor real: "))
    # mostra_valor(v_real)
    # valor1 = int(input("Digite o valor 1: "))
    # valor2 = int(input("Digite o valor 2: "))
    # mostra_2valores(valor1 , valor2)
def calcula_dobro(p_valor):
    dobro = p_valor * 2
    return dobro

def calcula_triplo(p_valor_1):
    triplo = p_valor_1 * 3
    return triplo

def soma(V1,V2):
    soma1 = V1 + V2
    return soma1

def soma_2(V1,V2):
    return V1 + V2

if __name__ == '__main__':
  valor = int(input("Digite um valor: "))
  v_retornado = calcula_dobro(valor)
  print(f"O dobro do número é: {calcula_dobro(valor)}")

  valor_1 = int(input("Digite um valor: "))
  retornado = calcula_triplo(valor_1)
  print(f"O triplo do número é: {retornado}")

  S1 = int(input("Digite o valor A: "))
  S2 = int(input("Digite o valor B: "))
  resultado = soma(S1,S2)
  print(f"A soma dos números é: {resultado}")

  a1= int(input("Digite um valor: "))
  b1 =int(input("Digite outro valor: "))
  print(f"A soma dos números é: {soma_2(a1,b1)}")