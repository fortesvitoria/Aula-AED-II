'''
Árvore AVL é um tipo de Árvore Binária de Busca (ABB) que se mantém automaticamente balanceada durante a inserção de novos elementos.
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def adicionar_no(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
        else:
            self.raiz = self._adicionar_no_folha(self.raiz, valor)

    def _adicionar_no_folha(self, no_atual, valor):
        # 1. Inserção normal de Árvore de Busca Binária
        if not no_atual:
            return No(valor)
        elif valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)

        # 2. Atualiza a altura do nó atual
        no_atual.altura = 1 + max(self._altura(no_atual.esquerda), self._altura(no_atual.direita))

        # 3. Obtém o fator de balanceamento
        balanceamento = self._balanceamento(no_atual)

        # 4. Casos de Rotação (Balanceamento)
        
        # Caso Esquerda-Esquerda
        if balanceamento > 1 and valor < no_atual.esquerda.valor:
            return self._rotacao_direita(no_atual)

        # Caso Esquerda-Direita
        if balanceamento > 1 and valor > no_atual.esquerda.valor:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Caso Direita-Direita
        if balanceamento < -1 and valor > no_atual.direita.valor:
            return self._rotacao_esquerda(no_atual)

        # Caso Direita-Esquerda
        if balanceamento < -1 and valor < no_atual.direita.valor:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def _altura(self, no):
        if not no:
            return 0
        return no.altura

    def _balanceamento(self, no):
        if not no:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, pai):
        filhoE = pai.esquerda
        neto = filhoE.direita
        
        # Realiza a rotação
        filhoE.direita = pai
        pai.esquerda = neto
        
        # Atualiza as alturas
        pai.altura = 1 + max(self._altura(pai.esquerda), self._altura(pai.direita))
        filhoE.altura = 1 + max(self._altura(filhoE.esquerda), self._altura(filhoE.direita))
        
        return filhoE

    def _rotacao_esquerda(self, pai):
        filhoD = pai.direita
        neto = filhoD.esquerda
        
        # Realiza a rotação
        filhoD.esquerda = pai
        pai.direita = neto
        
        # Atualiza as alturas
        pai.altura = 1 + max(self._altura(pai.esquerda), self._altura(pai.direita))
        filhoD.altura = 1 + max(self._altura(filhoD.esquerda), self._altura(filhoD.direita))
        
        return filhoD

    # Percorre a árvore em ordem crescente
    def percorrer_em_ordem(self, no):
        if no:
            self.percorrer_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.percorrer_em_ordem(no.direita)

numeros = [7, 80, 17, 99, 45, 53, 12]

arvore = ArvoreAVL()

for numero in numeros:
    arvore.adicionar_no(numero)

print("Lista original:\n", numeros)

print("\nLista árvore AVL: ")
arvore.percorrer_em_ordem(arvore.raiz)