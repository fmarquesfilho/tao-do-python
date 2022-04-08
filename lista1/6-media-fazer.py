'''
Escreva um programa que lê dois números reais, 
e imprime a média aritmética de ambos, com valor aproximado para
duas casas decimais. Depois disso o programa 
faz o seguinte:
- se a média é maior ou igual a 5, imprime "Aprovado"
- se a média está entre 8 e 10 (incluindo 8 e 10), 
imprime "Super aprovado"
- se a média é menor que 5, imprime "Recuperação" e solicita a nota
correspondente. 
- se o aluno obtiver mais do que 6 na recuperação, imprime "Aprovado", 
caso contrário imprime "Reprovado"
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
        print("Recuperação")
        rec = float(input("Digite a nota da recuperação: "))
        if rec >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
else:
    print("Digite notas entre 0 e 10.")
