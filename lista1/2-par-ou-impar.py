'''
Escreva um programa que lê dois números inteiros, 
e imprime uma mensagem caso ambos sejam pares ou
caso ambos sejam ímpares.
''' 
n1 = int(input("Digite o primeiro número inteiro: "))
resto1 = n1 % 2
n2 = int(input("Digite o segundo número inteiro: "))
resto2 = n2 % 2

if resto1 > 0 and resto2 > 0:
    print("Ambos são ímpares.")
elif resto1 == 0 and resto2 == 0:
    print("Ambos são pares.")
