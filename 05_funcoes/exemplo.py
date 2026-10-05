#Oque é uma função:

# Uma função é um bloco de código criado para realizar
# uma determinada tarefa.
#
# Ela permite organizar e reutilizar código.

#1. Criando uma função
#utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem vindo")

#para executar a função, chamamos seu nome
saudacao()

#2. Função com parâmetro

def saudacao(nome):
    print(f"\nOlá {nome}, seja bem vindo(a)!")


saudacao("Ana")
saudacao("Carlos")


# 3. Mais de um Parâmetro

def apresentar(nome, idade):
    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")


apresentar("Maria", 17)


# 4. Função com Cálculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")


somar(10, 5)

#5. Retornando um valor
#0 return devolve um valor para o loval onde
#a função foi chamada

def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(10, 5)
print(resultado)


# 6. Função com Condição

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificarIdade(20)
print(resultado)


# 7. Parâmetro com Valor Padrão
# Podemos definir um valor padrão para um parâmetro.

def saudacao(nome = "Aluno"):
    print(f"Olá {nome}")

saudacao()
saudacao("João")

#8. Varios parâmetros
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media
print(calcularMedia(8, 7, 9))

#9. Funcoes para orgnaizar um programa
def cadastraProduto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço"))
    return nome, preco

def exibirProduto():
    print("\n === Produtos cadastrados ===")
    print(f"nome {nome}")
    print(f"Preço: R${preco}")

    nome, preco = cadastrProduto()
    exibirProduto(nome, produto)