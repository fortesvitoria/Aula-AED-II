#criando pilha
class Pino:
    def __init__(self):
        self.argola = None
        self.topo = None

    def pino_vazio(self):
        if self.topo is None:
            return True
        return False

    def add(self, argola_nova):
        if self.pino_vazio():
            self.argola = argola_nova
            self.topo = argola_nova
            return

        self.topo.proximo = argola_nova
        self.topo = argola_nova

    def imprimir(self):
        print("\n-------- Pilha --------\n")
        if self.topo is None:
            print("-------- Pilha vazia --------\n")
            return 
        while self.argola: 
            print (f'Valor: {self.argola.valor} - Endereço: {id(self.argola)} - Próximo: {id(self.argola.proximo)}')
            self.argola = self.argola.proximo
        print(f"{"-"*25}")

#criando nó
class Argola:
    def __init__(self, valor: int):
        self.valor = valor
        self.proximo = None

a1 = Argola(10)
a2 = Argola(20)
a3 = Argola(30)

pino = Pino()
pino.add(a1)
pino.add(a2)
pino.add(a3)

pino.imprimir()