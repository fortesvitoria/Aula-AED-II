'''
Radix: 
- algoritmo de ordenação não comparativo. 
- distribuiu os elementos em buckets com base nos seus dígitos individuais (unidades, dezenas, centenas, etc.).
- a versão mais comum é a LSD (Least Significant Digit), que começa ordenando pelo dígito menos significativo (unidades) até o mais significativo.
- costuma-se usar o Counting Sort como sub-rotina para ordenar cada um dos dígitos de forma estável (mantendo a ordem relativa dos números com mesmo dígito).

'''

import exercicio01_gerador_lista as gl 
lista_gerada = gl.gerador_de_lista(10,20)

def counting_sort_por_digito(lista, exp):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10  # baldes de 0 a 9 para a base decimal

    # conta a frequencia de cada digito na posição 'exp'
    for i in range(n):
        digito = (lista[i] // exp) % 10
        contagem[digito] += 1

    # acumula os valores para determinar as posicoes finais
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    # constroi o array de saíia (de tres para frente para manter estabilidade)
    for i in range(n - 1, -1, -1):
        digito = (lista[i] // exp) % 10
        saida[contagem[digito] - 1] = lista[i]
        contagem[digito] -= 1

    # copia o resultado de volta para a lista original
    for i in range(n):
        lista[i] = saida[i]


def radix_sort(lista):
    if not lista:
        return lista

    # descobre o maior numero para saber quantas casas decimais processar
    maximo = max(lista)

    # aplica o counting sort para cada casa decimal: 1 (unidade), 10 (dezena), 100 (centena)...
    exp = 1
    while maximo // exp > 0:
        counting_sort_por_digito(lista, exp)
        exp *= 10

    return lista



print("Lista original:", lista_gerada)
radix_sort(lista_gerada)
print("Lista ordenada:",lista_gerada)