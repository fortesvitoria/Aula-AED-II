'''
faz a varredura comparando um elemento com o outro, 
e vai trocando de posição se o elemento da esquerda for maior que o da 
direita, até que a lista esteja ordenada.

'''

import exercicio01_gerador_lista as gl 
lista_gerada = gl.gerador_de_lista(10,20)


def bubble_sort(lista):

    tamanho_lista = len(lista)

    troca = False
    for i in range(tamanho_lista):
        for j in range(0, tamanho_lista-i-1):
            if lista[j] > lista[j+1]: #j+1, anterior+proximo
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca = True #flag validacao

        if troca:
            troca = False
        else:
            break

    return lista

print(lista_gerada)

print(bubble_sort(lista_gerada))