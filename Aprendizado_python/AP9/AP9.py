listM=[]
listF=[]
print("Digite  altura [0] para sair.")
print("[M]Masculino\n[F]feminino")
while True:
    A = str(input("Digite o gênero: "))
    B = float(input("Digite a altura: "))
    if B == 0 or A == '0':

        if max(listF) > max(listM):
            print(f"A maior altura do grupo é:{max(listF)}")
        else:
            print(f"A maior altura do grupo é:{max(listM)}")
        if min(listF) < min(listM):
            print(f"A menor altura do grupo é:{min(listF)}")
        else:
            print(f"A menor altura do grupo é:{min(listM)}")
        print(f"Quantidade de homens: {len(listM)}\nQuantidade de mulheres: {len(listF)}")
        break
    if A =='M' or A == 'm':
        listM.append(B)
    elif A == 'F' or A == 'f':
        listF.append(B)
    else:
        print("Genero inválido.")
