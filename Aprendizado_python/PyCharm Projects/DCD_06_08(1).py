A = 5
B = 3
print(f"{A}+{B}={A + B}") #adição
print(f"{A}-{B}={A - B}") #subtração
print(f"{A}*{B}={A * B}") #multiplicação
print(f"{A}/{B}={A / B}") #divisão
print(f"{A}^{B}={A ** B}") #potência
print(f"{A}//{B}={A // B}") #divisão que retorna a parte inteira
print(f"{A}%{B}={A % B}") #mostra o resto da divisão
print(f"Raiz quadrada = 9**0.5") #fórmula para raiz quadrada
print(f"raiz quadrada de {A}={A**0.5:.2f} e raiz quadrada de {B}={B**0.5:.2f}")

idade = 15
print(idade > 18) #maior que
print(idade < 18) #menor que
print(idade >= 15) #maior ou igual
print(idade <= 15) #menor ou igual
print(idade == 18) #igual
print(idade != 18) #diferente
while True:
    C = int(input("Digite a idade: "))
    if C < 0 or C > 1000:
        break
    if C <= 3:
        print("Bebê")
    elif C <= 12:
        print("Criança")
    elif C <= 17:
        print("Adolescente")
    elif C <=59:
        print("Adulto")
    else:
        print("Idoso")