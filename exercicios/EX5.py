# -*- coding: utf-8 -*- #permitir acentos
from math import sqrt


a = int(input("insira o 1° número: "))
c = input("Insira  o sinal da operação: ")
b = int(input("insira o 2° número: "))

while(True):

	if(c == '+'):
		resultado = a + b
		print(resultado)
		break;

	elif(c == '-'):
		resultado = a - b
		print(resultado)
		break;

	elif(c == '*'):
		resultado = a * b
		print(resultado)
		break;

	elif(c == '/'):
		resultado = a / b
		print(resultado)
		break;

	elif(c == '**' or c == '^'):
		resultado = a ** b
		print(resultado)
		break;

	else:
		print("operador invalido: ")
		c = input("Insira  o sinal da operação: ")






		
