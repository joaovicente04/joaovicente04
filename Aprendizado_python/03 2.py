N=str(input('Nome:'))
A=int(input('Ano de nascimento: '))
C=2025-A
if C>=16 and C<18:
    print(f'''Ano de nascimento: {A}.
{N}
Idade: {C}.
Tem idade para votar''')
elif C>=18 and C>16:
    print(f'''Ano de nascimento: {A}.
{N}
Idade:{C}
Tem idade para votar e tirar a CNH''')
else:
    print(f'''Ano de nascimento: {A}.
{N}    
Idade: {C}
Não tem idade para votar''')
