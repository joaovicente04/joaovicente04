soma=0
ct=0
for A in range (1,11):
    if A<=10:
        A=A*2
    soma=soma+A
    print(A, end=' ')
    ct=ct+1
media= soma/ct
print(f'\nA soma dos numeros é: {soma}')
print(f'\nA média dos números é: {media}')

