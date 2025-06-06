from difflib import diff_bytes


def soma(a,b):
    C = a + b
    print(f"{a}+{b}={C}")
def subt(a,b):
    C = a - b
    print(f"{a}-{b}={C}")
def mult(a,b):
    C = a * b
    print(f"{a}x{b}={C}")
def div(a,b):
    C = a / b
    print(f"{a}/{b}={C}")
if __name__ == '__main__':
    A = int(input("Digite um número: "))
    B = int(input("Digite outro número: "))
    print("Operações:[+],[-],[*],[/] ")
    D = str(input("Digite a operação: "))
    if D == "+":
        soma(A,B)
    elif D == "-":
        subt(A,B)
    elif D == "*":
        mult(A,B)
    elif D == "/":
        div(A,B)