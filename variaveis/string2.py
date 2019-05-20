# -*- utf-8 -*-

''' tipo de dado que armazena coleção de texto
declaradas entre aspas'''

a = "Diego"
b = "Mariano"
concatenar = a + ' ' + b + "\n" #quebra de linha '\n'

print(concatenar)
print(concatenar.lower()) #passa pra minusculo

print(concatenar.upper()) #passa para minusculo

print(concatenar.strip()) #remove caracter especial

minhaString = "O rato roeu a roupa do rei de Roma"



minhaLista = minhaString.split(" ") #separa string no espaço
print(minhaLista)

minhaLista = minhaString.split("o") #separa string na letra o 
#minuscula
print(minhaLista)

"""Busca de substrings
substring = pedaço de string
"""
busca = minhaString.find("rei") #fala posição em que encontra-se
#a palavra
print(busca)

minhaString = minhaString.replace("do", "da") #substitui string
minhaString = minhaString.replace("rei", "rainha")
print(minhaString)

