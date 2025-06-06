def fatorial (a):
    fat = 1
    for i in range(1,a+1):
        fat = fat*i
    print(f"O fatorial de {a} é: {fat}")

if __name__ == '__main__':
    A = int(input("Digite um número: "))
    fatorial(A)