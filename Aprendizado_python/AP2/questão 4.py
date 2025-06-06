A=float(input('Digite um numero: '))
B=float(input('Digite outro numero: '))
print('''Adição{A}
Subtração{S}
Multiplicação{M}
Divisão{D}''')
O=str(input('Digite a operação: '))
if O=='A':
    print(f'{A}+{B} é:',(A+B))
elif O=='S':
    print(f'{A}-{B} é:',(A-B))
elif O=='M':
    print(f'{A}*{B} é:',(A*B))
elif O=='D':
    print(f'{A}/{B} é:',(A/B))
else:
    print('resposta inválida.Digite novamente.')
