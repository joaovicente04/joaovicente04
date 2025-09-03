# Listas []
from numpy.ma.extras import median

from DCD_20_08_tuplas import idade

frutas = ["maça","banana","uva","laranja"]

# print(frutas[0])
# print(frutas[1])
# print(frutas[-1])


# print(len(frutas))
# print(frutas.count("banana"))
# print(frutas.index("uva"))
# for fruta in frutas:
#     print(fruta)

#Modificando Listas
frutas[0] = "abacaxi"
# print(frutas)

# Adicionar
frutas.append("maça")
# print(frutas)

frutas.insert(2,"pera")
# print(frutas)

# Remover itens
frutas.remove("uva")
# print(frutas)
#
# print(frutas.pop())
# print(frutas)
del frutas [0]
# print(frutas)

# Ordenar de forma crescente
frutas.sort()
#print(frutas)
# inverter a ordem
frutas.reverse()
#print(frutas)
idades = [23,45,12,2,98,56]
print(idades)
#idades.sort(reverse= True)
idades.sort()
print(idades)
idades.reverse()
print(idades)

# Erro, tipos diferentes
misto = [1, "oi", 3.1415, True]
#misto.sort()
#print(misto)

# Soma de todos os elementos

soma = sum(idades)
print(soma)
media = sum(idades) / len(idades)
print(media)