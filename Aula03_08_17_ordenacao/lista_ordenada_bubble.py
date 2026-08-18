
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

                atual = atual.proximo #atual avança para o próximo nodo.

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

# ordenando
lista_encadeada.ordem_crescente_bubble_sort()

# mostra a lista ordenada
atual = lista_encadeada.inicio #variavel atual recebe inicio da lista
lista_ordenada = [] #cria lista

while atual is not None: #enquanto atual não for nulo
    lista_ordenada.append(atual.dado) #append no dado do atual
    atual = atual.proximo #atual recebe o proximo que irá repeterir o looping

print(f"Lista ordenada: {lista_ordenada}")