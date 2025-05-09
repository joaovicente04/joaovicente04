#usuario fornece valor inicial e final.
ct=0
soma=0
A=int(input("Digite o valor inicial da sequência: "))
B=int(input("Digite o valor final da sequência: "))
if A <B:         #ordem crescente
    print("[Valores na ordem crescente]")
    for C in range (A, B+1, 1) :
        ct += 1
        soma = soma + C
        print( C, end=" ")
elif A == B: #valores iguais ==
    print("[Os valores são iguais]")
else:         #ordem decrescente
    print("[=Valores na ordem decrescente]")
    for C in range(A, B-1, -1) :
        ct += 1
        soma = soma + C
        print(C, end=" ")

print(f"\nA quantidade de números é: {ct}")
print(f"A soma dos números é: {soma}")