#Listas, Tuplas e Dicionários

#1. Listas

#Listas são utilizadas para armazenar vários valores
# dentro de unica variavel.

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

#2.Acessando elementos da Lista

print(nomes[0])
print(nomes[1])

# Podemos acessar o ultimo elemento usando -1
print(nomes[-1])

#3. Alterando elementos

#As listas são mutáves, ou seja, os elementos podem se alterados
nomes[0] = "Pedro"
print(nomes)

#4. Adicionando Elementos
#append() adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição