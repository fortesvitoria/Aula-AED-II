import json
import os

class No:
    def __init__(self, nome, tipo, tamanho = None):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

def carregar_no(dados): #funcao recursiva para converter o dic do js em objetos da classe
    no = No(
        nome = dados["nome"],
        tipo = dados ["tipo"],
        tamanho = dados.get("tamanho") #se nao existir, retorna none
    )

    for filho_dados in dados.get("filhos",  []): # se for diretorio e tiver filhos, carrega filho recursivamente
        no.adicionar_filho(carregar_no(filho_dados))

    return no

def pre_ordem(no, nivel = 0):
    if no is None:
        return

    #visita o no atual e imprime
    indenta = "." * nivel
    info_tamanho = f"({no.tamanho} bytes)" if no.tamanho is not None else ""
    print(f"{indenta} [{no.tipo.upper()}] {no.nome} {info_tamanho}")

    for filho in no.filhos:
        pre_ordem(filho, nivel + 1)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(diretorio_atual, 'sistema_arquivos.json')

with open(caminho_json, 'r', encoding='utf-8') as f:
    sistema_arquivos = json.load(f)

raiz = carregar_no(sistema_arquivos)

pre_ordem(raiz)