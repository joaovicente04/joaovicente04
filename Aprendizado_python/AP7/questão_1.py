def valor(a):

    if a>0:
        print("Valor positivo.")
    elif a == 0:
        print('valor nulo.')
    else:
        print("Valor negativo.")
if __name__ == '__main__':
    A = int(input("Digite um número: "))
    valor(A)