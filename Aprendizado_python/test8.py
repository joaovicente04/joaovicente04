A=float(input('preço de compra:'))
B=float(input('preço de venda:'))
if A>B:
    print('teve prejuízo.')
elif A==B:
    print('Os valores são iguais.')
else:
    print('Teve lucro.')