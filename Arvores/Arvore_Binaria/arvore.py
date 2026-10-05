class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        return self.raiz is None

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def inserir(self, valor):
        novo_no = No(valor)

        if self.vazia():
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _encontrar_menor_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def _excluir_recursivo(self, no_atual, valor):
        if no_atual is None:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._excluir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._excluir_recursivo(no_atual.direita, valor)
        else:
            # Caso 1: Nó sem filhos (folha)
            if no_atual.esquerda is None and no_atual.direita is None:
                return None
            # Caso 2: Nó com um filho
            elif no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            # Caso 3: Nó com dois filhos
            else:
                # Encontrar o menor valor na subárvore direita
                menor_valor = self._encontrar_menor_valor(no_atual.direita)
                no_atual.valor = menor_valor
                no_atual.direita = self._excluir_recursivo(no_atual.direita, menor_valor)

        return no_atual


    def excluir(self, valor):
        self.raiz = self._excluir_recursivo(self.raiz, valor)

    def imprimir_em_ordem(self, no=None):
        if self.vazia():
            print("------ Árvore vazia ------")
            return

        if no is None:
            no = self.raiz

        if no.esquerda is not None:
            self.imprimir_em_ordem(no.esquerda)

        print(no.valor)

        if no.direita is not None:
            self.imprimir_em_ordem(no.direita)

lista = [50, 30, 70, 20, 40, 60, 80]
arvore = ArvoreBinaria()

for valor in lista:
    arvore.inserir(valor)
    
arvore.imprimir_em_ordem()