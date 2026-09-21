
'''
Merge sort: Dividir para Conquistar. 

Ele funciona em três etapas básicas:

- Divide a lista ao meio até restar apenas sublistas de 1 elemento (que já estão ordenadas).
- Ordena as sublistas menores.
- Junta (intercala) duas listas ordenadas em uma nova lista totalmente ordenada.

'''

import exercicio01_gerador_lista as gl 
lista_gerada = gl.gerador_de_lista(10,20)

def merge_sort(lista):
    # se a lista tiver 1 ou 0 elementos, ja esta ordenada
    if len(lista) <= 1:
        return lista

    # divide a lista em duas metades e guarda  as metades
    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]

    # aplica o merge_sort recursivamente em cada metade (chamando o metodo novamente)
    esquerda_ordenada = merge_sort(metade_esquerda)
    direita_ordenada = merge_sort(metade_direita)

    # intercala as duas metades ordenadas
    return merge(esquerda_ordenada, direita_ordenada)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # compara os elementos das duas listas e adiciona o menor no resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # adiciona os elementos restantes de qualquer uma das listas
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

ordenada = merge_sort(lista_gerada)

print("Lista original:", lista_gerada)
print("Lista ordenada:", ordenada)