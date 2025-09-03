# #Remoção de espaços
frase_2 = " Olá, mundo!  "

# print(frase_2)
# print(frase_2.strip())  #Remove espaços nas pontas
# print(frase_2.lstrip()) #Remove espaços no início
# print(frase_2.rstrip()) #Remove espaços no final

frase_3 = "#Exemplo#"
# print(frase_3.strip("#")) #Remove caractere específico nas pontas

# # Substitui conteúdo de substring (pedaço da string)
mensagem = "Olá Marcos!"
# print(mensagem)
# nova_mensagem = mensagem.replace("Marcos", "Maria")
# print(nova_mensagem)

# # Verifica se existe o conteúdo dentro da string
frase_4 = "A IA irá dominar o mundo"
# print("IA" in frase_4)
# print("AI" in frase_4)
# print(frase_4.startswith("A"))      # Verifica se string inicia com valor
# print(frase_4.endswith("mundo"))    # Verifica se string termina com valor

#Verifica comprimento da string
palavra = "computador"
# print(len(palavra)) #contagem de letras/tamanho da palavra
# print(palavra.count("o")) #quantidade de caracteres correspondentes
# print(palavra.count("om"))

#Divisão e junção de strings
frase_5 = "Aprender Python é divertido"
# lista_palavras = frase_5.split()
# print(lista_palavras)
# frase_6 = "-".join(lista_palavras)
# print(frase_6)

# Encontrar posições
frase_7 = "Python é muito Versátil"
# print(frase_7.find("é"))
# print(frase_7.find("Java"))
# print(frase_7.index("Versátil"))

#FORMATAÇÕES
nome ="João"
idade = 20
altura = 1.8564522
# print("Olá, meu nome é "+nome+" e tenho "+str(idade)+" anos.")
# print("Olá, meu nome é",nome,"e tenho",idade,"anos.")
# print("Olá, meu nome é {} e tenho {} anos.".format(nome,idade))
# print("Olá, meu nome é {1} e tenho {0} anos.".format(nome,idade))
# print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
# import math
# #FORMATAÇÃO DE FLOAT
# print(f"{nome} tem {altura:.2f}")
# print(math.floor(altura)) #arredenda pra baixo
# print(math.ceil(altura))  #arredonda pra cima

# TUPLA () COM DADOS DE UM CLIENTE
cliente = ("José",62, "Brasilia")
# print("Nome:",cliente[0])
# print("Idade:",cliente[1])
# print("Cidade:",cliente[2])
# A tupla não permite alterações
#cliente[0] = "Maria"

cores = ("vermelho","verde","azul","violeta","carmim")
# for cor in cores:
#     print(cor)
#
# print(len(cores))
# print(cores.count("vermelho"))
# print(cores.index("azul"))