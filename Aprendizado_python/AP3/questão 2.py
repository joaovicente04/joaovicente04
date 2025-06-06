B=0
R=0
ct=0
print('Para sair digite [0]')
while True:
    A=float(input("Digite uma nota: "))
    ct+=1
    if A==0:
        break
    elif A>=5:
        B+=1
    elif A<5:
        R+=1
print("Quantidade de alunos aprovados: ",B)
print('Quantidade de alunos reprovados: ',R)
print('Numero de notas: ',ct)
