'''
No BFS, utilizamos uma fila para visitar os vizinhos.

No Dijkstra, utilizamos um dicionário de distâncias e uma lista de cidades 
visitadas para escolher sempre a menor distância acumulada.
'''

from Grafos.bfs import Fila


class Nodo:
    def __init__(self, cidade):
        self.cidade = cidade
        self.vizinhos = []

    def adicionar_vizinho(self, nodo, distancia):
        self.vizinhos.append((nodo, distancia))

class Grafo:
    def __init__(self):
        self.nodos = {}

    def adicionar_cidade(self, cidade):
        if cidade not in self.nodos:
            self.nodos[cidade] = Nodo(cidade)

    def conectar(self, origem, destino, distancia):
        self.nodos[origem].adicionar_vizinho(self.nodos[destino], distancia)
        self.nodos[destino].adicionar_vizinho(self.nodos[origem], distancia)

    def dijkstra(self, cidade_inicial):
        visitados = []
        fila = Fila()
        fila.enfileirar(self.nodos[cidade_inicial])

        while not fila.esta_vazia():
            atual = fila.desenfileirar()

        if atual.cidade not in visitados:
            print(atual.cidade)
            visitados.append(atual.cidade)
            
        for vizinho in atual.vizinhos:
            if vizinho.cidade not in visitados:
                fila.enfileirar(vizinho)