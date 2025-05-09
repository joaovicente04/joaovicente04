ct=0
soma=0
D=str(input('disciplina: '))
print('Para sair digite [0]')
while True:
    A=float(input("Digite uma nota: "))
    if A==0:
        break
    elif A%2==0:
        ct=ct+1
        soma=soma+A       #soma += A
    elif A>0:
       B= ct=ct+1
if ct==0:
    print('Não posso dividir por zero')

else:
    M=soma/ct
    print("média das notas pares é: ",M)
    print('Disciplina: ',D)
    print('Numero de notas: ',ct)
    print('Quantidade de notas: ',B)

