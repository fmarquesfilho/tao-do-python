'''
Escreva um programa que lê dois números reais, 
e imprime a média aritmética de ambos, com valor aproximado para
duas casas decimais. Depois disso o programa 
faz o seguinte:
- se a média é maior ou igual a 5, imprime "Aprovado"
- se a média está entre 8 e 10 (incluindo 8 e 10), 
imprime "Super aprovado"
''' 

f1 = float(input("Digite o primeiro número: "))
f2 = float(input("Digite o segundo número: "))

if f1 >= 0 and f1 <= 10 and f2 >= 0 and f2 <= 10:
    media = (f1 + f2) / 2
    print("A média entre {} e {} é {:.2f}".format(f1, f2, media))
    if media >= 8:
        print("Super aprovado")
    elif media >= 5:
        print("Aprovado")
else:
    print("Digite notas entre 0 e 10.")
