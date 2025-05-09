V=float(input('Digite o valor da compra:'))
V1=float(input("Digite o valo da venda:"))
if V>V1:
    print('compra:',V,'venda:',V1,',Teve prejuizo de:',V-V1)
elif V==V1:
    print('os valores são iguais')
else:
    print('compra:',V,'venda:',V1,',teve lucro de:', V1-V)
