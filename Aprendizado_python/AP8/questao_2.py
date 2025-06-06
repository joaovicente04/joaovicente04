list = []
print("Digite[-1] para sair")
while True:
    A = int(input("Digite um Número: "))
    if A not in list:
        list.append(A)
    if A == -1:
        print(f"A quantidade de alunos é: {len(list)}")
        print(f"A média da turma é: {sum(list)/len(list)}")