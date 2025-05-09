#notas de alunos
ct=0
soma=0
C= int(input("digite a quantidade de alunos: "))
for A in range(0,C,1):
    B=float(input("Digite a nota: "))
    ct += 1
    soma = soma + B
media = soma / ct
print(f"A soma das notas é {soma}")
print(f"A média das notas é: {media}")
