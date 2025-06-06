def mensagem (num,msg):
    M = print(f"Informações digitadas: {num} e {msg}")

if __name__ == '__main__':
    A = int(input("Digite um numero: "))
    B = str(input("Digite uma mensagem: "))
    C= mensagem(A,B)
    print(C)