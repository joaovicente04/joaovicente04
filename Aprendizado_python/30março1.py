ct=0     #contador
maior=-9999999#maior
menor=9999999 #menor valor
soma=0 #somador
print("Digite [0] para sair")   # o que o usuario vai digitar
while True:
    A= int(input('Digite um Número: ')) #valor de entrada
    if A==0:
        break
    if A>maior:
        maior=A
    if A<menor:
        menor=A
    soma=soma+A
    ct=ct+1
print(f'O menor valor é {menor}')
print(f'A soma dos valores é: {soma}')
print(f'A quantidade de valores digitados é: {ct}')
print(f"O maior valor é {maior}")
