def soma_3 (N1,N2,N3):
    S=N1+N2+N3
    print(f"A soma de {N1} + {N2} + {N3} = {S}")
    return S

if __name__ == '__main__':

    A=int(input("Digite o primeiro número: "))
    B=int(input("Digite o segundo número: "))
    C=int(input("Digite o terceiro número: "))
    soma_3(A,B,C)