#crie uma função para saber se um número digitado pelo usuário é par ou impar e mostre o dobro e o triplo desse número

def função (valor):
    if valor%2 == 0:
        C = valor * 2
        D = valor * 3
        print(f"Numero par, o dobro do seu número é {C} e o triplo é {D}")
    else:
        C = valor * 2
        D = valor * 3
        print(f"Numero impar, o dobro do seu número é {C} e o triplo é {D}")
    return C,D

if __name__ == '__main__':
    A = int(input("Digite o seu número: "))
    função(A)