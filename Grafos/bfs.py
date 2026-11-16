'''
BFS encontra o menor caminho em quantidade de passos (arestas)
não de distâncias.
O Dijkstra encontra o menor caminho em custo (peso)
'''

class Nodo:
    def __init__(self, cidade):
        self.cidade = cidade
        self.vizinhos = []

    def adicionar_vizinho(self, nodo):
        self.vizinhos.append(nodo)

class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        
    def esta_vazia(self):
        return len(self.itens) == 0

class Grafo:
    def __init__(self):
        self.nodos = {}

    def adicionar_cidade(self, cidade):
        self.nodos[cidade] = Nodo(cidade)

    def conectar(self, origem, destino):
        self.nodos[origem].adicionar_vizinho(self.nodos[destino])
        self.nodos[destino].adicionar_vizinho(self.nodos[origem])

    def bfs(self, cidade_inicial):
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