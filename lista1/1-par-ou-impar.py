'''
Escreva um programa que lê um número inteiro, 
e imprime se esse número é par ou ímpar.
''' 
n = int(input("Digite um número inteiro: "))
resto = n % 2
if resto > 0:
    print("O número digitado é ímpar.")
else:
    print("O número digitado é par.")
