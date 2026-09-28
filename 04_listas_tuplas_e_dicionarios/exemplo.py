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
nomes.insert(1, "Mariana")
print(nomes)

#5. Removendo Elementos
#remove() remove o um elemento pelo seu valor
nomes.remove("Lucas")
print(nomes)

#pop() remove o um elemento pelo índice
nomes.pop(0)
print(nomes)

#6. Tamanho da lista

# len() informa a quantidade de elementos.
print(len(nomes))

#7. Percorrendo uma lista.

for nome in nomes:
     print(nome)

#8. Verificando se um elemento existe

if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")

    #9. Lista com com diferentes tipos de dados

    dados = ["João", 18, 1.75, True]
    print(dados)

    #10. Lista de números
    notas = [7.5, 8.0, 6.5, 9.0]
    soma = 0

    media = soma / len(notas)
    print(f"Média: {media:.1f}")

#11. Tuplas
# Tuplas são semelhantes às listas.
# A principal diferença é que tuplas não podem
# ser alteradas depois de criadas.

coordenadas = (10, 20)
print(coordenadas)

#acessando elementos
print(coordenadas[0])
print(coordenadas[1])

#12. Dicionários
# Dicinários armazenam informações no formato:
# chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}
print(aluno)

#13. Acessando valor do diciário
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

#14. Alterando valores

aluno["nota"] = 9.0
print(aluno)