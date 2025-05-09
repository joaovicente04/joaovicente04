
ct=0
soma=0
print('Digite[] para sair.')
D=str(input('Disciplina: '))
while True:
    num= int(input('Digite as notas da turma: '))
    if num==0:
        break
    ct= ct+1
    soma=soma+num
media=soma/ct
print('Disciplina: ',D)
print('quantidade de alunos: ',ct)
print(f'média das notas: {media:.2f}')