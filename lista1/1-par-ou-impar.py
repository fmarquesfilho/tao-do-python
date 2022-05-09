'''
Escreva um programa que lê um número inteiro, 
e imprime se esse número é par ou ímpar.
''' 

# Recebe um número inteiro e retorna verdadeiro caso ele seja par e falso
# quando ele for ímpar.
def par(i):
    r = i % 2
    return r == 0

def impar(i):
    return not par(i)

mensagem = "Digite um número inteiro: "
entrada = input(mensagem)
i = int(entrada)

if impar(i):
    print("O número é ímpar.")
else:
    print("O número é par.")
