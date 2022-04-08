'''
Escreva um programa que lê um número inteiro e imprime os
5 números inteiros subsequentes. Por exemplo:
Digite um número inteiro: 5
6
7
8
9
10
< fim de execução >
''' 

n = int(input("Digite um número inteiro: "))

i = 0
while i < 5:
    print(n + i + 1)
    i = i + 1
