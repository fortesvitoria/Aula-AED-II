class Lista:
    def __init__(self):
        self.inicio = None #Inicia a lista com valor nulo

    def add(self, valor): 
        nodo = No(valor) #guarda memoria uma instancia da classe Nó com seu valor

        if self.inicio is None: #verifica se vazia 
            self.inicio = nodo #se estiver vazia, add o valor da instacia da classe Nó // 1. RECEBE "D" 

        else:
            if nodo.dado < self.inicio.dado: #se o dado do nodo é menor que inicio // 2. SE "A" FOR MENOR QUE "D" // 3. "C" < "A"? NÃO // 4. B < A ? Não
                nodo.prox = self.inicio #prox do nó recebe o que esta no inicio // 2. RECEBE "D"
                self.inicio = nodo #inicio recebe nodo // 2. RECEBE "A"

            else: 
                ant = self.inicio # 2. ANTERIOR RECEBE "A"
                aux = self.inicio.prox #aux recebe o prox do inicio // 2. AUXILAR RECEBE O PROX DO INICIO "D" 

                while aux : #enquanto existir aux, continua
                    if nodo.dado < aux.dado: #Se o dado do Nó for menor que o dado do auxiliar // 3. dado do Nó "C" < AUX DADO "D"? SIM //4. "B" < aux C? sim
                        nodo.prox = aux #proximo recebe aux //3.  PROX DO NÓ "C" RECEBE "D" // 4. recebe C
                        ant.prox = nodo #anterior do proximo recebe nodo ;//3. PROX DO ANTERIOR "A" RECEBE "C" // 4. recebe "B"
                        break #3. [A] -> [C] -> [D] - > None
                    else:
                        ant = aux #anterior recebe aux
                        aux = aux.prox #aux recebe o proximo

                if aux == None:
                    ant.prox = nodo #proximo do anterior recebe nodo

            self.imprimir()

    def imprimir(self):
        print("\n---- Lista encadeada ----\n")
        if self.inicio is None:
            print("XXXX Lista vazia XXXX\n")
            return 
        aux = self.inicio
        while aux: 
            print(aux.dado)
            aux = aux.prox
        print(f"{"-"*25}")

    def remover(self,valor):
        removeu = False
        if self.inicio == None:
            print("XXXX Lista vazia XXXX\n")
        else: 
            #verifica se o valor está na primeira posição
            if valor  == self.inicio.dado: 
                self.inicio = self.inicio.prox # o inicio passa a ser o proximo do inicio
                removeu = True
            else: # quando a lista nao for vazia e quando o valor não é igual ao primeiro - testa a partir do segundo elemento
                ant = self.inicio #inicio ja testado
                aux = self.inicio.prox #testando o segundo elemento
                while aux: #enquanto aux for diferente de null/enquanto existir
                    if valor == aux.dado:
                        ant.prox = aux.prox #elemento anterior aponta para o proximo do que sera deletado
                        removeu = True
                        break
                    else:
                        # auxiliar nao é igual ao valor que quero remover, testo o proximo. estrutura para seguir percorrendo a lista
                        ant  = aux
                        aux = aux.prox
            if removeu:
                print(f"{valor} - Elemento removido!")
            else:
                print(f"{valor} - Não encontrado!")
            self.imprimir()