'''
Escreva um programa que lê dois números inteiros, 
e imprime uma mensagem caso ambos sejam pares ou
caso ambos sejam ímpares. Ele não fala nada quando
um é par e o outro é ímpar.
''' 
# Recebe um número inteiro e retorna verdadeiro caso ele seja par e falso
# quando ele for ímpar.
def par(i):
    r = i % 2
    return r == 0

def impar(i):
    return not par(i)

x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

if par(x) and par(y):
    print("Ambos são pares.")

if impar(x) and impar(y):
    print("Ambos são ímpares.")

