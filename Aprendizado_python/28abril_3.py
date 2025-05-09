#importando biblioteca
import random
ct1=0
ct2=0
ct3=0
ct4=0
ct5=0
ct6=0
B=int(input("Digite a quantidade de repeticões: "))
C=int(input("Digite o inicio da sequência: "))
D=int(input("Digite o final da sequência: "))
print("Numeros sorteados: ")
for A in range(1,B):
    N = random.randint(C, D)
    if N == 1:
        ct1=ct1+1
    elif N == 2:
        ct2=ct2+1
    elif N == 3:
        ct3= ct3+1
    elif N == 4:
        ct4= ct4+1
    elif N == 5:
        ct5 = ct5+1
    elif N ==6:
        ct6 = ct6+1
    print(N, end=" ")
p1 = ct1/B
p2 = ct2/B
p3 = ct3/B
p4 = ct4/B
p5 = ct5/B
p6 = ct5/B

print(f"\nQuantidade de 1: {ct1}, porcentagem:{p1 :.2f}%")
print(f"Quantidade de 2: {ct2}, porcentagem:{p2 :.2f}%")
print(f"Quantidade de 3: {ct3}, porcentagem:{p3 :.2f}%")
print(f"Quantidade de 4: {ct4}, porcentagem:{p4 :.2f}%")
print(f"Quantidade de 5: {ct5}, porcentagem:{p5 :.2f}%")
print(f"Quantidade de 6: {ct6}, porcentagem:{p6 :.2f}%")