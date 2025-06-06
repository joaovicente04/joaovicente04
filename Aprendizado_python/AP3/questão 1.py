maior_que_20=0
ct=0
soma=0
print('Para sair digite [0]')
while True:
    A=float(input("Digite um valor: "))
    if A==0:
        break
    elif A>0:
        ct=ct+1
        soma=soma+A       #soma += A
    if A>20:
        maior_que_20 +=1
if ct==0:
    print('Não posso dividir por zero')

else:
    M=soma/ct
    print("A média dos números é: ",M)
    print('A soma dos números é ',soma)
    print('A quantidade de números é: ',ct)
    print('Quantidade de numeros maior que 20 é: ',maior_que_20)
