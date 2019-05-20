# -*- coding: utf-8 -*- #permitir acentos
from math import sqrt


a = [3,2,1]
a = sorted(a) #oderna
print(a)

lista = [1,3,4,5,12]

for i in range(len(lista)):
	menor = i #recebe o primeiro elemento
	for j in range(i+1, len(lista)): 

		if(lista[j] < lista[menor]):
			menor = j
	if lista[i] != lista[menor]:
	auxiliar = lista[i]
	lista[i] = lista[menor]
	lista[menor] = auxiliar

print(lista)

		
