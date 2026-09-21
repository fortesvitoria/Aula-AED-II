'''
Quick sort: 

- Escolhe um Pivô, seleciona um elemento da lista para ser a referência.
- Reorganiza a lista para que todos os elementos menores que o pivô fiquem à sua esquerda e todos os maiores fiquem à sua direita.
- Aplica o mesmo processo recursivamente nas sublistas da esquerda e da direita.

'''

import exercicio01_gerador_lista as gl 
lista_gerada = gl.gerador_de_lista(10,20)

def quick_sort(lista):
    # se a lista tiver 1 ou 0 elementos, ja esta ordenada
    if len(lista) <= 1:
        return lista

    # escolhe o pivo (utilizando elemento que esta no meio)
    pivo = lista[len(lista) // 2]

    # particiona a lista em tres sublistas
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    # chama a recursao nas sublistas e junta o resultado
    return quick_sort(menores) + iguais + quick_sort(maiores)


ordenada = quick_sort(lista_gerada)

print("Lista original:", lista_gerada)
print("Lista ordenada:", ordenada)