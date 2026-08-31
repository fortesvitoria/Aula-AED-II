
import exercicio01_gerador_lista as gl 
lista_gerada = gl.gerador_de_lista(10,20)

class Nodo:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo_nodo = Nodo(valor)

        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def ordem_crescente_select_sort(self):
        atual = self.inicio #atual recebe inicio/head

        while atual is not None: #enquanto atual nao for vazio
            menor = atual #menor recebe o atual
            proximo = atual.proximo #proximo recebe o proximo do atual

            while proximo is not None: #enquanto o proximo nao for vazio
                if proximo.dado < menor.dado: #se o dado do proximo for menor que o dado da variavel menor
                    menor = proximo #menor recebe o proximo
                proximo = proximo.proximo #proximo recebe o proximo do proximo/avança na busca pelo menor

            if menor != atual: # se o menor for diferetente do atual, troca
                atual.dado, menor.dado = menor.dado, atual.dado
                # print (f'Troca atual {menor.dado} - menor {atual.dado}')

            atual = atual.proximo #atual recebe o proximo do atual/avança o inicio da parte ainda nao ordenada

    def ordem_crescente_bubble_sort(self):
        if self.inicio is None:
            return
        #flag de controle
        trocou = True

        while trocou:
            #trocou começa com false
            trocou = False
            atual = self.inicio #atual recebe o nodo

            while atual.proximo is not None: #enquanto o proximo nao for none
                if atual.dado > atual.proximo.dado: #se o dado for maior que o proximo
                    atual.dado, atual.proximo.dado = ( #dado recebe o dado do proximo e o proximo recebe o dado
                        atual.proximo.dado,
                        atual.dado
                    )
                    trocou = True #flag vira true
                    print(atual.dado)
                    print(atual.proximo.dado)

                atual = atual.proximo #atual avança para o próximo nodo.

    def insertion_sort(self):
        # 1. [5,3,4,1]
        atual = self.inicio.proximo #comecamos pelo segundo 1. atual = 3

        while atual is not None:
            valor = atual.dado #guarda valor que quero inserir na posição correta 1. valor=3
            anterior = self.inicio #anterior recebe o inicio 1. anterior = 5

            while anterior != atual and anterior.dado <= atual.dado: #procura onde deve estar
                #1. 5<=3 False, ant-5, atual-3, val-3
                anterior = anterior.proximo

            if anterior != atual: #quando encontramos posição anterior, vamos deslocando os valores - 1. true
                while anterior.proximo != atual: #anterior.proximo é o atual - 3, entao False, while nao excecuta
                    anterior.dado, valor = valor, anterior.dado
                    anterior = anterior.proximo

                atual.dado = valor #coloca valor guadado na posição que sobrou 1. atual = 3

            atual = atual.proximo


    def buscar(self, valor):
        atual = self.inicio
        posicao = 0
        while atual is not None:
            if atual.dado == valor:
                return posicao, atual.dado
            atual = atual.proximo
            posicao += 1
        return None, None


lista_encadeada = Lista()

# inserindo elementos da lista gerada na lista encadeada
for numero in lista_gerada:
    lista_encadeada.inserir(numero)

print(f"Lista gerada: {lista_gerada}")


# SELECT SORT

# ordenando BUBBLE
# lista_encadeada.ordem_crescente_bubble_sort()

# ordenando SELECT
# lista_encadeada.ordem_crescente_select_sort()

# ordenando INSERT
lista_encadeada.insertion_sort()

# mostra a lista ordenada
atual = lista_encadeada.inicio #variavel atual recebe inicio da lista
lista_ordenada = [] #cria lista

while atual is not None: #enquanto atual não for nulo
    lista_ordenada.append(atual.dado) #append no dado do atual
    atual = atual.proximo #atual recebe o proximo que irá repeterir o looping

print(f"Lista ordenada: {lista_ordenada}")
