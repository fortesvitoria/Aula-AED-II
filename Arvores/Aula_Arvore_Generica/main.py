from no import No
from arvore import Arvore

def menu():
    print("\n============== ÁRVORE DE ARQUIVOS ==============\n")
    print("1 - Mostrar árvore em pré-ordem")
    print("2 - Mostrar árvore em pós-ordem")
    print("3 - Buscar arquivo ou diretório")
    print("4 - Mostrar altura da árvore")
    print("5 - Consultar profundidade")
    print("6 - Mostrar folhas")
    print("7 - Mostrar caminho de um elemento")
    print("8 - Calcular tamanho de um diretório")
    print("9 - Buscar arquivos por extensão")
    print("10 - Mostrar estatísticas")
    print("11 - Diretório com maior número de arquivos")
    print("0 - Encerrar")
    print("\n------------------------------\n")

    op = input("Digite a opção desejada: ")
    return op

opcao = -1
while opcao != "0":
    opcao = menu()
    if opcao == "1":
        pass