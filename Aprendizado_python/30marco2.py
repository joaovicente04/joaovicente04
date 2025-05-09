ctg=0  #contador geral
soma=0
maior_altura=0
menor_altura=3
cth=0
ctm=0
while True:
    print('Digite[m] para masculino e [f] para feminino\nDigite[0] para sair')
    G=str(input('Digite o gênero: '))
    if G=='0':
        break
    A=float(input('Digite a altura: '))
    if A>maior_altura:
        maior_altura=A
    if A<menor_altura:
        menor_altura=A
    if G=='m':
        cth=cth+1
    if G=='f':
        ctm=ctm+1
    if A>0:
        soma=soma+A
        ctg=ctg+1
media=soma/ctg
print(f'maior altura: {maior_altura}')
print(f'menor altura: {menor_altura}')
print(f'quantidade de homens: {cth}')
print(f'quantidade de mulheres: {ctm}')
print(f'média das alturas: {media}')
