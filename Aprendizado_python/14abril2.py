ct=0
soma=0
print('-ORDEM DECRESCENTE-')
for A in range(7,-1,-1):
    soma = soma + A
    ct = ct + 1
    print(A,end=' ')
media=soma/ct
print(f'\nQuantidade de variáveis: {ct}')
print(f'Soma das variáveis: {soma}')
print(f'A média das váriaveis é: {media}')

