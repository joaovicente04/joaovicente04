print('Homem-H')
print('Mulher-M')
G=(input('Digite o genero:'))
P=float(input('Digite a altura:'))
if G=='M':
    print('o peso ideal é:',(62.1*P)-44.7)
elif G=='H':
    print('o peso ideal é:',(72.7*P)-58)
else:
    print()