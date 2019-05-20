# -*- coding: utf-8 -*- #permitir acentos
from math import sqrt

'''funcao open pra abrir
variavel = open(modo)

r = somente leitura
w = escrita(caso ele ja exista, sera apagado e um novo arquivo em branco sera criado)
a = leitura e escrita (adiciona o novo conteudo ao fim do arquivo)
r+ = leitura e escrita
w+ = escrita(apaga o conteudo anterior do arquivo)
a+ = leitura e escrita(abre arquivo para atualização)

read() le arquivo inteiro
readline() le uma linha
readlines() le arquivo e o armazena em uma lista'''

arquivo = open("arqAula1.txt")
linhas = arquivo.readlines()

print(arquivo) #printa informaçoes do arquivo somente

print(linhas) #salva linhas em uma lista e printa

for linha in linhas:
	print (linha) #imprime linha por linha

txtCompleto = arquivo.read()

print(txtCompleto) #salva todo o texto numa variavel inteira

#criando arquivo __________________________________________________

w = open('arquivo criado pelo python na aula1.txt', 'w')

w.write("esse é o meu arquivo") #escrevendo dentro do arquvio

w.close() #fecha arquivo


w = open('arqAula1.txt', 'w') #apaga conteudo arqAula1.txt  e insere conteudo novo (write)

w.write("esse é o meu arquivo")

w.close() 

w = open('arqAula1.txt', 'a') #adiciona conteudo em arqAula1.txt  no fim da linha  (write)

w.write("\nesse é o meu arquivo \n")

w.close() 