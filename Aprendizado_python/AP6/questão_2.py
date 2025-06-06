def calcula (ano_nascimento):
    C= 2025-ano_nascimento
    print(f"A idade é: {C}")
    return C

if __name__ == '__main__':
    A=int(input("Digite o ano de nascimento: "))
    if A > 2025:
        print('Ano inválido.')
    else:
        calcula(A)
