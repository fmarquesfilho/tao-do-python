'''
Escreva um programa que lê um número inteiro e imprime os
X números inteiros subsequentes, sendo X um valor inteiro
informado pelo usuário. Por exemplo:
Digite um número inteiro: 5
Quantos inteiros você deseja imprimir a partir do 5? 3
6
7
8
< fim de execução >
''' 

n = int(input("Digite um número inteiro: "))
k = int(input("Quantos números você deseja imprimir a partir do {}? ".format(n)))

i = 0
while i < k:
    print(n + i + 1)
    i = i + 1