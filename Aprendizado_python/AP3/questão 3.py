cp=0 #contador par
P=0
I=0
ci=0  #contador ímpar
print('Para sair digite [0]')
while True:
    A=float(input("Digite um número: "))
    if A==0:
        break
    elif A%2==0:
        cp=cp+1
        P=P+A
    elif A%2==1:
        ci=ci+1
        I=I+A

print("média dos números pares: ",P/cp)
print('Média dos números ímpares',I/ci)


