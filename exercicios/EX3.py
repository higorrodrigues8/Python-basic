# -*- coding: utf-8 -*- #permitir acentos
from math import sqrt
t = 1

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

		
delta = b**2 - 4*a*c

if delta > 0:
	raiz = sqrt(delta)
	x1 = (-b + raiz)/(2*a)
	x2 = (-b - raiz)/(2*a)
	print(x1)
	print(x2)
		
