ct=0
C=int(input('Digite o valor inicial decrescente: '))
for A in range(C,-1,-1):
    ct=ct+1
    if A !=0:
        print(A,end='->')
    else:
        print(A,end='.')
print(f'\nA quantidade de valores é: {ct}')