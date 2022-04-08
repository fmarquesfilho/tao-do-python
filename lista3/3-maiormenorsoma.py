'''
  Modifique o programa abaixo apenas no local indicado.
  Dado um conjunto de N números inteiros fornecido pelo usuário, 
  determine o menor valor, o maior valor e a soma dos valores do conjunto.
'''

n = int(input("quantos números você deseja digitar? entre com um número inteiro positivo: "))

if n > 0:
    x = int(input("digite um número inteiro: "))
    maior = x
    menor = x
    soma = x

    i = 2
    while i <= n:
        x = int(input("digite um número inteiro: "))
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
        soma = soma + x
        i = i + 1

    print("A soma dos números é {}. O maior número é {} e o menor é {}.".format(soma, maior, menor))
else:
    print("O número de elementos do conjunto deve ser um inteiro positivo (maior do que zero")
