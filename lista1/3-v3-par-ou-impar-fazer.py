'''
Escreva um programa que lê dois números inteiros, 
e imprime uma mensagem caso apenas um dos números
seja ímpar e o outro seja par. O programa não 
deve dizer nada quando ambos foram pares ou
quando ambos forem ímpares.
''' 
# Recebe um número inteiro e retorna verdadeiro caso ele seja par e falso
# quando ele for ímpar.
def par(i):
    r = i % 2
    return r == 0

def impar(i):
    return not par(i)


def diferentes(a, b):
    return (par(a) or par(b)) and (impar(a) or impar(b))


x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))
 
if diferentes(x, y):
    print("um número é ímpar e o outro é par.")

