# Dicionários {}

#alunos = {"nome" : "Ana", "idade" : 20,"nota" : 8.2}
aluno = {
    "nome" : "Ana",
    "idade" : 20,
    "nota" : 8.2
}
print(aluno)
print(alunos["nome"])
print(alunos["idade"])
print(alunos["nota"])

aluno["nota"] = 9.0
aluno["curso"] = "CDM"
del aluno["idade"]
#print(aluno)

for chave,valor in aluno.items():
    print(f"{chave} -> {valor}")

# Verificando existência de chave
if "curso" in aluno:
    print(f"Curso {aluno["curso"]}")
else:
    print("Curso não informado")

print(aluno.keys())     #Retorna todas as chaves
print(aluno.values())   #Retorna todos os valores
print(aluno.items())    #Retorna todos os pares chave:valor

nome = input("Digite o nome do aluno:")
nota = float(input("Digite a nota do aluno:"))

cadastro = {
    "nome" : nome,
    "nota" : nota
}

print(f"{cadastro["nome"]} tirou a nota: {cadastro["nota"]}")

alunos = [
    {"nome":"João", "nota": 7.2},
    {"nome":"Kleber", "nota": 8.2},
    {"nome":"Joana", "nota": 9.2}
]

for a in alunos:
    print(f"{a["nome"]} tirou a nota {a["nota"]}")