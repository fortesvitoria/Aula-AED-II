'''
Eficiência e Complexidade (Big-O)
A grande vantagem da busca binária sobre a busca sequencial é a sua velocidade em grandes conjuntos de dados:

    Busca Sequencial: Tem complexidade O(n) (tempo linear), pois no pior caso você olha todos os n elementos.
    Busca Binária: Tem complexidade O(logn) (tempo logarítmico). Isso significa que, se você dobrar o tamanho da lista, a busca binária precisará de apenas um passo extra para encontrar o item, enquanto a sequencial precisaria do dobro de passos.

-------------------------------------------------------

Como Funciona o AlgoritmoPré-requisito: 
A lista de dados precisa estar em ordem (crescente ou decrescente).
Passo 1: Encontre o índice do meio (meio) da lista atual.
Passo 2: Olhe o item no índice do meio.
Passo 3: Se o item for o alvo, retorne sua posição.
Passo 4: Se o alvo for menor que o meio, descarte a metade direita e busque na esquerda.
Passo 5: Se o alvo for maior, descarte a metade esquerda e busque na direita.

'''
import exercicio01_gerador_lista as gl 
contador = 0 #para verificar etapas

def busca_binaria(lista_gerada, encontrar_valor):
    global contador #global para funcionar dentro e fora da função 
    indice_inical = 0
    indice_final = len(lista_gerada)-1

    while indice_inical <= indice_final:
        contador += 1
        indice_meio = (indice_inical+indice_final) // 2

        if encontrar_valor == lista_gerada[indice_meio]:
            return indice_meio

        if encontrar_valor < lista_gerada[indice_meio]:
            indice_final = indice_meio - 1

        else:
            indice_inical = indice_meio + 1

lista_gerada = gl.gerador_de_lista(10, 10)
lista_ordenada = sorted(lista_gerada)
elemento_busca = 7

print(f"Lista gerada: {lista_gerada}")
print(f"Lista ordenada: {lista_ordenada}")

print(f"O número {elemento_busca} está na posição {busca_binaria(lista_ordenada, elemento_busca)} - Foram feitos {contador} loop(s).")