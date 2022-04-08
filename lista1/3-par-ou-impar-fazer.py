'''
Escreva um programa que lê dois números inteiros, 
e imprime uma mensagem caso apenas um dos números
seja ímpar e o outro seja par.
''' 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resto1 = n1 % 2
resto2 = n2 % 2

if resto1 != 0 and resto2 == 0:
    print("O primeiro número é ímpar e o segundo é par.")
elif resto1 == 0 and resto2 != 0:
    print("O primeiro número é par e o segundo é ímpar.")
