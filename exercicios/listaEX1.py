
idade = int(input("Insira sua idade \n"))

if idade >= 18:
    print("Você é maior de idade")
    
elif ((idade < 18) and (idade > 0)):
    print("Você é menor de idade")

else:
    print("Dados inválidos")