#BUSCA SEQUENCIAL ORDENADA

import random

# Variaveis globais
lista = []
chaves = []
n = 10  # quantidade de números na sequencia


# busca sequencial
def busca_binaria(sequencia, chave):
    inicio = 0
    fim = len(sequencia) - 1

    # Caso chave seja igual ao valor do mio, retorna posição
    # Caso maior que chave posição atual se torna novo começo
    # Caso menor que chave posição atual se torna novo fim
    # Caso chave não encontrada

    while inicio <= fim:
        #define o meio inteiro da lista
        meio = (inicio + fim) // 2

        # Caso chave seja igual ao valor do mio, retorna posição
        if chave == sequencia[meio]:
            return meio
        # Caso maior que chave posição atual se torna novo começo
        elif chave < sequencia[meio]:
            fim = meio - 1
        # Caso menor que chave posição atual se torna novo fim
        else:
            inicio = meio + 1
        #Caso chave não encontrada
        return -1

# Quantidade de chaves a serem encontradas
q = int(input("Número de chaves a serem encontradas:"))

# Criando lista com valores aleatórios
for _ in range(n):
    lista.append(random.randint(0, 20))

# Criando chaves com valores aleatórios5
for _ in range(q):
    chaves.append(random.randint(0, 20))

#Imprimindo lista
print(lista)

#Oerdenando lista
lista = sorted(lista)

#Imprimindo lista ordenada
print(lista)


for w in range(q):

    # Chama busca sequencial
    resultado = busca_binaria(lista, chaves[w])

    # Verificação do elemento
    if resultado != -1:
        print(f'O elemento {chaves[w]} foi encontrado no índice {resultado}.')
    else:
        print(f'O elemento {chaves[w]} não está na lista.')

