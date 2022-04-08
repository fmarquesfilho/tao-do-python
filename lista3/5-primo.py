'''
Os números primos possuem várias aplicações dentro da Computação, por exemplo na 
Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''

x = int(input("digite um número inteiro: "))
divisores = 0   # contador do número de divisores que x tem

i = 1
while i <= x:
    if x % i == 0:
        divisores = divisores + 1
    i = i + 1

if divisores == 2:
    print("{} é primo.".format(x))
else:
    print("{} não é primo.".format(x))
    