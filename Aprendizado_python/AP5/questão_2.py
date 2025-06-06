A=int(input("Digite o valor inicial: "))
B=int(input("Digite o valor final: "))
if B>A:
    for i in range(A,B+1):
        C = (5 * (i - 32)) / 9
        print(f"{i} F° | {C:.2f} C°")
elif B<A:
    for i in range(A,B+1,-1):
        C = (5 * (i - 32)) / 9
        print(f"{i} F° | {C:.2f} C°")



