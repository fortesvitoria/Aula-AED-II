import os
import string

class No:
    def __init__(self, palavra, frequencia=1):
        self.palavra = palavra
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self, raiz=None):
        # Cada nó da árvore deve armazenar: - Palavra; - Quantidade de ocorrências da palavra no texto
        self.raiz = raiz
        self.total_palavras_lidas = 0

    def _normalizar_palavra(self, palavra):
        # Converte para minúsculo e remove pontuações.
            palavra = palavra.lower()
            palavra = palavra.translate(str.maketrans('', '', string.punctuation))
            return palavra

    def inserir(self, palavra):
        palavra_normalizada = self._normalizar_palavra(palavra)

        #ignora strings vazias ou apenas com espaços em branco
        if not palavra_normalizada.strip():
            return
        self.total_palavras_lidas += 1
        self.raiz = self._inserir_recursivo(self.raiz, palavra_normalizada)

    def _inserir_recursivo(self, no_atual, palavra):
        if no_atual is None:
            return No(palavra)

        if palavra < no_atual.palavra:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, palavra)
        elif palavra > no_atual.palavra:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, palavra)
        else:
            no_atual.frequencia += 1

        return no_atual


    def buscar(self, palavra):
        palavra_normalizada = self._normalizar_palavra(palavra)
        return self._buscar_recursivo(self.raiz, palavra_normalizada)

    def _buscar_recursivo(self, no_atual, palavra):
        if no_atual is None:
            return None

        if palavra < no_atual.palavra:
            return self._buscar_recursivo(no_atual.esquerda, palavra)
        elif palavra > no_atual.palavra:
            return self._buscar_recursivo(no_atual.direita, palavra)
        else:
            return no_atual

    def imprimir_em_ordem(self, no=None, primeira_chamada=True):
        if primeira_chamada and self.raiz is None:
            print("\n------ Árvore vazia ------")
            return

        if primeira_chamada:
            no = self.raiz

        if no is None:
            return

        self.imprimir_em_ordem(no.esquerda, False)
        print(f"Palavra: {no.palavra} | Frequência: {no.frequencia}")
        self.imprimir_em_ordem(no.direita, False)

    def contar_nos(self,no=None, primeira_chamada=True):
        if primeira_chamada:
            no = self.raiz
        if no is None:
            return 0
        return 1 + self.contar_nos(no.esquerda, False) + self.contar_nos(no.direita, False)

    def contar_folhas(self, no=None, primeira_chamada=True):
        if primeira_chamada:
            no = self.raiz
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        return self.contar_folhas(no.esquerda, False) + self.contar_folhas(no.direita, False)

    def calcular_altura(self, no=None, primeira_chamada=True):
        if primeira_chamada:
            no = self.raiz
        if no is None:
            return -1 # Árvore vazia tem altura -1 
        
        altura_esquerda = self.calcular_altura(no.esquerda, False)
        altura_direita = self.calcular_altura(no.direita, False)

        return 1 + max(altura_esquerda, altura_direita)  

    def _coletar_todos_nos(self, no, nos):
        if no is not None:
            nos.append(no)
            self._coletar_todos_nos(no.esquerda, nos)
            self._coletar_todos_nos(no.direita, nos)

    def obter_palavra_mais_frequente(self):
        if self.raiz is None:
            return None

        todos_nos = []
        self._coletar_todos_nos(self.raiz, todos_nos)

        palavra_mais_frequente = max(todos_nos, key=lambda no: no.frequencia)
        return palavra_mais_frequente.palavra, palavra_mais_frequente.frequencia

    def exibir_top_10(self):
        if self.raiz is None:
            print("Árvore vazia.")
            return

        todos_nos = []
        self._coletar_todos_nos(self.raiz, todos_nos)

        # Ordena os nós pela frequência em ordem decrescente
        nos_ordenados = sorted(todos_nos, key=lambda no: no.frequencia, reverse=True)

        print("\nTop 10 palavras mais frequentes:")
        for i, no in enumerate(nos_ordenados[:10]):
            print(f"{i + 1}. Palavra: {no.palavra} | Frequência: {no.frequencia}")

    def processar_texto(self, texto):
        palavras = texto.split()
        for palavra in palavras:
            self.inserir(palavra)


#MENU
def main():
    arvore = None
    
    while True:
        print("\n===== MENU =====")
        print("1 - Iniciar nova árvore com Texto Digitado")
        print("2 - Iniciar nova árvore lendo de um Arquivo Texto")
        print("3 - Buscar palavra")
        print("4 - Exibir índice em ordem alfabética")
        print("5 - Mostrar estatísticas do texto")
        print("6 - Mostrar informações da árvore")
        print("7 - Exibir as 10 palavras mais frequentes")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            texto = input("\nDigite ou cole o texto desejado:\n> ")
            arvore = ArvoreBinaria()
            arvore.processar_texto(texto)
            print("\n[Sucesso] Texto processado e indexado na árvore!")

        elif opcao == "2":
            caminho = input("\nDigite o nome do arquivo .txt (padrão: texto.txt): ").strip()
            if not caminho:
                caminho = "texto.txt"

            try:
                diretorio_atual = os.path.dirname(os.path.abspath(__file__))
                caminho_arquivo = os.path.join(diretorio_atual, caminho)

                with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                    texto = arquivo.read()
                    arvore = ArvoreBinaria()
                    arvore.processar_texto(texto)
                    print(f"\n[Sucesso] Arquivo '{caminho}' lido e indexado na árvore!")
            except FileNotFoundError:
                print(f"\n[Erro] O arquivo '{caminho}' não foi encontrado na pasta.")
            except Exception as e:
                print(f"\n[Erro inesperado]: {e}")


        elif opcao == "3":
            if arvore is None or arvore.raiz is None:
                print("\n[Aviso] A árvore está vazia. Insira um texto primeiro.")
                continue
            palavra_busca = input("\nDigite a palavra que deseja buscar: ")
            resultado = arvore.buscar(palavra_busca)
            if resultado:
                print(f"\n[Encontrado] A palavra '{resultado.palavra}' aparece {resultado.frequencia} vez(es).")
            else:
                print(f"\n[Não Encontrado] A palavra '{palavra_busca}' não está presente no índice.")

        elif opcao == "4":
            if arvore is None or arvore.raiz is None:
                print("\n[Aviso] A árvore está vazia.")
            else:
                print("\n===== ÍNDICE EM ORDEM ALFABÉTICA =====")
                arvore.imprimir_em_ordem()

        elif opcao == "5":
            if arvore is None or arvore.raiz is None:
                print("\n[Aviso] A árvore está vazia.")
            else:
                mais_freq_palavra, mais_freq_qtd = arvore.obter_palavra_mais_frequente()
                print("\n===== ESTATÍSTICAS DO TEXTO =====")
                print(f"Total de palavras lidas (com repetição): {arvore.total_palavras_lidas}")
                print(f"Total de palavras distintas (nós): {arvore.contar_nos()}")
                print(f"Palavra mais frequente: '{mais_freq_palavra}'")
                print(f"Quantidade de ocorrências: {mais_freq_qtd}")

        elif opcao == "6":
            if arvore is None or arvore.raiz is None:
                print("\n[Aviso] A árvore está vazia.")
            else:
                print("\n===== INFORMAÇÕES DA ÁRVORE =====")
                print(f"Altura da árvore: {arvore.calcular_altura()}")
                print(f"Quantidade de nós (distintos): {arvore.contar_nos()}")
                print(f"Quantidade de folhas: {arvore.contar_folhas()}")

        elif opcao == "7":
            if arvore is None or arvore.raiz is None:
                print("\n[Aviso] A árvore está vazia.")
            else:
                arvore.exibir_top_10()

        elif opcao == "0":
            print("\nEncerrando o programa. Até mais!")
            break
        else:
            print("\n[Opção Inválida] Escolha uma opção válida do menu.")

if __name__ == "__main__":
    main()