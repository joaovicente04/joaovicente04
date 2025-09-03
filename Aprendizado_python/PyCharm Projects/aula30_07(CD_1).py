import turtle as tl
A = int(input("Digite o numero de lados: "))
C = 360/A
for B in range (A):
    tl.right(C)
    tl.forward(10)
print(f"Os angulo externo é de: {C}")
tl.done()
