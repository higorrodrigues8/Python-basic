# -*- coding: utf-8 -*- #permitir acentos
from math import sqrt


minhaLista = ['abacaxi', 'melancia', 'abacate']

minhaListaInt = [1,3,4,5,6,7]

minhaLista_3 = ["abacaxi", "abacate", 1, 3, 4, 5, 6, True]

listaNull = []
print(minhaLista[2]) #printa somento o item correspondente ao indice

for item in minhaLista: #percorre a lista desque o item esteja nela
 	print(item)
tamanho = len(minhaLista) #len = tamanho da lista

print(tamanho) #printa o tamanho

minhaLista.append("Limao") #adiciona item, por padrao no fim
print(minhaLista)

if 71 in minhaListaInt:
	print("7 esta na lista")

del minhaLista[2:] #remove item do indice 2 ate o ultimo
	print(minhaLista)

del minhaLista[:] #apaga todos os itens




