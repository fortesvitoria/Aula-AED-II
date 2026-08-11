'''
Crie uma função que receba como parametro a quantidade de elementos e o valor final a ser gerado 
aleatoriamente e retorne uma lista com esses elementos, iniciando do zero.

Exemplo: gerador_de_listas_inteiro(10,50)

10 -> quantidade de elementos
50 -> elementos entre 1 e 50

lista = random.sample(range(0,intervalo_max), tam_lista)

'''

import random

def gerador_de_lista(quantidade, valor):
    lista = []
    for _ in range(quantidade):
        lista.append(random.randint(0,valor)) #a = valor inicial (0) / b = valor final
    return lista

lista_gerada = gerador_de_lista(10,10)

print(f"Lista: {lista_gerada}")

'''
Busca sequencial ou busca por exaustão
Cria uma função que receba a lista gerada e a informação a ser encontrada.
Essa função deverá retirbar a posição da lista onde a informalção foi encontrada 
ou retornar none se não enciontrada.
'''

def encontrar_item(lista_gerada, item):
    for numero in lista_gerada:
        if item == numero:
            return lista_gerada.index(item)
    return None
# encontrar_item(lista_gerada, 2)
busca = random.choice(lista_gerada)
print(f"Item: {busca} na posição: {encontrar_item(lista_gerada, busca)}")

# --------------------- Codigo do professor ---------------------

def busca_seq (lista_entrada: list, elemento_loc: int) -> int:
    for indice, elemento in enumerate(lista_entrada):
        if elemento == elemento_loc:
            return indice
    return None

elemento_proc = random.choice(lista_gerada)
print(f"Elemento {elemento_proc} na posição: {busca_seq(lista_gerada, elemento_proc)}")

# Com nomes
lista_nome = ["Ana", "Bruno", "Carlos", "Eduardo"]
elemento_nome = random.choice(lista_nome)
print(f"Nome {elemento_nome} na posição: {busca_seq(lista_nome, elemento_nome)}")



