# media / mediana / moda

from statistics import *
'''
mean(lista)
median(lista)
mode(lista)
'''

def media(lista):
	media = sum(lista)/float(len(lista))
	return media
def mediana(lista):
	listaOrdenada = sorted(lista)
	t = len(listaOrdenada)
	if(t % 2 == 0):
		mediana = (listaOrdenada[int(t/2)] + listaOrdenada[int((t/2)-1)])/2
	elif(t % 2 == 1):
		mediana = listaOrdenada[int((t/2))]
		return mediana