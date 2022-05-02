'''
Escreva um programa que lê um número inteiro, 
e imprime se esse número é par ou ímpar.
''' 
def par(i):
    resto = i % 2
    if resto == 0:
        return True
    else:
        return False

def impar(i):
    return not par(i)

mensagem = "Digite um número inteiro: "
entrada = input(mensagem)
i = int(entrada)

if par(i):
    print("O número é par.")

if impar(i):
    print("O número é ímpar.")
