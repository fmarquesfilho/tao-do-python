'''
  Um problema do programa implementado no exercício anterior é que o usuário 
  precisa saber a priori o número de elementos do conjunto.

  Modifique o exercício anterior (3-maiormenorsoma.py) de modo que 
  o usuário possa digitar quantos números quiser. O programa deve terminar
  quando o usuário digitar a palavra "sair" (sem as aspas).

  Antes de terminar, o programa deve fazer exatamente como no exercício anterior,
  ou seja, imprimir o maior e menor números do conjunto, bem como a soma dos 
  elementos do conjunto.
'''

# inicialização das variáveis
primeira_vez = True
fim = False

while not fim:
    entrada = input("digite um número inteiro ou sair: ")
    if entrada == "sair":
        # sair do programa
        fim = True
        if primeira_vez:
            print("Nenhum número foi digitado. Até logo!")
        else:
            print("A soma dos números é {}. O maior número é {} e o menor é {}.".format(soma, maior, menor))
    else:
        x = int(entrada) # entrada é um número inteiro
        if primeira_vez:
            maior = x
            menor = x
            soma = x
            primeira_vez = False
        else:
            if x > maior:
                maior = x
            elif x < menor:
                menor = x
            soma = soma + x
