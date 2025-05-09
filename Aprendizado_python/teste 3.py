N1=float(input("Nota 1:"))
N2=float(input("Nota 2:"))
M=(N1+N2)/2
print(f'Média:{M:.2f}')
if M>=5 and M<7:
    print("MM Aluno aprovado")
elif M>=7 and M<10:
    print('MS Aluno aprovado!!')
elif M>=1 and M<5:
    print("II Aluno reprovado")
else:
    print("MI Aluno reprovado")