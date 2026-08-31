from gerador_nums_inteiros import lista_de_inteiros
from lista import Lista
from nodo import Nodo


def adicionar_numeros_na_lista(minha_lista):
    for num in lista_de_inteiros:
        minha_lista.adicionar(Nodo(num))



lista_ED = Lista()
adicionar_numeros_na_lista(lista_ED)
lista_ED.print()
# print("ok")
# elemento_localizar = int(input("Localizar o elemento: "))
# input(f"Vou localizar o elemento {elemento_localizar}")
# print(lista_ED.index(elemento_localizar))

lista_ED.ordena_bubble()
lista_ED.print()
