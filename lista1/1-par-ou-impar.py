'''
Escreva um programa que lê um número inteiro, 
e imprime se esse número é par ou ímpar.
''' 
# Soma dois inteiros e retorna o resultado. Recebe como entrada
#

def soma(a: int, b: int):
    x = a + b
    return x

def subtrai(a, b):
    x = a - b
    return x

som = soma(4, 3)
sub = subtrai(4, 3)

a = 5
a = sub
a = soma(a, sub)

mensagem_soma = "A soma é"
print(mensagem_soma, a)
print("A subtração é", sub)
