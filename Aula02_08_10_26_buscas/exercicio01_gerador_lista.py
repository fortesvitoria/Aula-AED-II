'''
Crie uma função que receba como parametro a quantidade de elementos e o valor final a ser gerado 
aleatoriamente e retorne uma lista com esses elementos, iniciando do zero.

Exemplo: gerador_de_listas_inteiro(10,50)

10 -> quantidade de elementos
50 -> elementos entre 1 e 50
'''

import random

#função para gerar lista com numeros aleatórios
def gerador_de_lista(quantidade, valor):
    # lista = []
    for _ in range(quantidade):
        # lista.append(random.randint(0,valor)) #a = valor inicial (0) / b = valor final
        #random.sample para não repetir valores, recebe valor inicial, valor final e quantidade de itens
        lista_inteiros = random.sample(range(0,valor),quantidade)
    return lista_inteiros

#lista gerada com 10 elementos entre 0 e 20
lista_gerada = gerador_de_lista(10,20)

# print(f"Lista: {lista_gerada}")
