A=float(input("Digite o valor do lado A: "))
B=float(input("Digite o valor do lado B: "))
C=float(input("Digite o valor do lado C: "))
if A+B>C and A+C>B and B+C>A:
    if A==B==C:
        print("É um triangulo equilatero.")
    elif A==B and A!=C or B==C and C!=A or A==C and A!=B:
        print("É um triangulo isosceles.")
    elif A!=B and A!=C and B!=C:
        print("É um triangulo escaleno.")
else:
    print('Não é um triangulo.')
