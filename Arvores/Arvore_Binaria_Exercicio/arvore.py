import string

class No:
    def __init__(self, palavra, frequencia=1):
        self.palavra = palavra
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, palavra):
        self.raiz = self._inserir(self.raiz, palavra)

    def _inserir(self, no_atual, palavra):
        if no_atual is None:
            return No(palavra)

        if palavra < no_atual.palavra:
            no_atual.esquerda = self._inserir(no_atual.esquerda, palavra)
        elif palavra > no_atual.palavra:
            no_atual.direita = self._inserir(no_atual.direita, palavra)
        else:
            no_atual.frequencia += 1

        return no_atual

    def _normalizar_palavra(self, palavra):
        palavra = palavra.lower()

        palavra = palavra.translate(
            str.maketrans('', '', string.punctuation)
        )

        return palavra

    def buscar(self, palavra):
        palavra_normalizada = self._normalizar_palavra(palavra)
        return self._buscar(self.raiz, palavra_normalizada)

    def _buscar(self, no_atual, palavra):
        if no_atual is None:
            return None

        if palavra < no_atual.palavra:
            return self._buscar(no_atual.esquerda, palavra)
        elif palavra > no_atual.palavra:
            return self._buscar(no_atual.direita, palavra)
        else:
            return no_atual

    def imprimir_em_ordem(self, no=None):
        if self.raiz is None:
            print("------ Árvore vazia ------")
            return

        if no is None:
            no = self.raiz

        if no.esquerda is not None:
            self.imprimir_em_ordem(no.esquerda)

        print(no.palavra, no.frequencia)

        if no.direita is not None:
            self.imprimir_em_ordem(no.direita)


palavra = input("Digite uma palavra para inserir na árvore: ")
lista = ["banana", "maçã", "laranja", "banana", "maçã", "uva"]
lista.append(palavra)

arvore = ArvoreBinaria()

for valor in lista:
    arvore.inserir(valor)
    
arvore.imprimir_em_ordem()