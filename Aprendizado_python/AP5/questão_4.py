soma=0
for A in range(1,500+1,1):
    if A%2!=0 and A%3==0:
        soma=soma+A
print(f"\nA soma de todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três é: {soma} ")