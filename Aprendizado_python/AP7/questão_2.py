def valor_abs(a):
    if a > 0:
        print(f"Absoluto={a}")
    elif a == 0:
        print("Valor nulo.")
    elif a < 0:
        print(f"Valor absoluto= {a*(-1)}")
if __name__ == '__main__':
    A = int(input("Digite um número: "))
    valor_abs(A)