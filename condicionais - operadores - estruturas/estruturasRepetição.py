# -*- utf-8 -*-

x = 1 
while x < 10: #enquanto

	print(x)
	x += 1 #x = x + 1
vetor = [1,2,3,4,5] #vetor de inteiro
vetor2 = ["ola", "mundo", "!"] #vetor de string
vetor3 = [0, "ola", "biscoito", "bolacha", 9.99, 1, 2, True] 
# ^ vetor int, string, string, string, float, int, int, bool

for i in vetor: #percorre vetor, i = conteudo da posição
	print(i)

#contagem começã do 0

'''for range = lista com elementos limitados comecando em 0'''
for i in range(10):
	print(i)

for i in range(10,20): #10 ate o ultimo numero menos 1
	print(i)

for i in range(10, 20, 2): #de 10 ate 19 de 2 em 2
	print(i)