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

x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

# exemplo usando o operador lógico not
if par(x) and impar(y):
    print("x é par e y é ímpar.")

if impar(x) and par(y):
    print("x é ímpar e y é par.")
