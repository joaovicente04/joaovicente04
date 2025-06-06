print('"Digite tres valores: "')
A=int(input('1: '))
B=int(input('2: '))
C=int(input('3: '))
if A>B and A>C:
    print('O maior valor é: ',A)
elif B>A and B>C:
    print('O maior valor é: ',B)
elif C>A and C>B:
    print('O maior valor é: ',C)
elif A==B and A==C:
    print('Os valores são iguais.')
else:
    print()