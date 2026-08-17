'''
Criar uma estrutura de dados com classes nodo e lista, e criar um método que localize o elemento na lista, retornando o elemento e sua posição na estrutura de dados.
'''
import random
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

# buscando com um item aleatório da lista
elemento = random.choice(lista_gerada)
posicao, valor = lista_encadeada.buscar(elemento)

print(f"Lista gerada: {lista_gerada}")
print(f"Busca pelo valor {elemento}: Encontrado na posição {posicao} com o valor {valor}.")