import exercicio01_gerador_lista as gl 
import random

'''
Busca sequencial ou busca por exaustão
Cria uma função que receba a lista gerada e a informação a ser encontrada.
Essa função deverá retirbar a posição da lista onde a informalção foi encontrada 
ou retornar none se não enciontrada.
'''

def encontrar_item(lista_gerada, item):
    for numero in lista_gerada:
        if item == numero:
            return lista_gerada.index(item) #retorna o index do item encontrado
    return None

# Gerar a lista
lista_gerada = gl.gerador_de_lista(10, 20)

busca = random.choice(lista_gerada)
print(f"Item: {busca} na posição: {encontrar_item(lista_gerada, busca)}")

# --------------------- Codigo do professor ---------------------

# Uso do enumerate(): fornece o índice e o elemento simultaneamente. 
# Performance: Em listas muito grandes, evitar o método .index() dentro do laço economiza tempo de processamento.

def busca_seq (lista_entrada: list, elemento_loc: int) -> int:
    for indice, elemento in enumerate(lista_entrada):
        if elemento == elemento_loc:
            return indice
    return None

print(f"Elemento {busca} na posição: {busca_seq(lista_gerada, busca)}")

# Com nomes
lista_nome = ["Ana", "Bruno", "Carlos", "Eduardo"]
elemento_nome = random.choice(lista_nome)
print(f"Nome {elemento_nome} na posição: {busca_seq(lista_nome, elemento_nome)}")

