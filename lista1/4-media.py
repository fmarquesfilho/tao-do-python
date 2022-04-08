'''
Escreva um programa que lê dois números reais, 
e imprime a média aritmética de ambos, com valor aproximado para
duas casas decimais.
''' 
f1 = float(input("Digite o primeiro número: "))
f2 = float(input("Digite o segundo número: "))

media = (f1 + f2) / 2

print("A média entre {} e {} é {:.2f}".format(f1, f2, media))