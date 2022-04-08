'''
  Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
  Ex.: 5!=5.4.3.2.1=120
  Dica: use while (comando de repetição)
'''
n = int(input("digite o número para o qual deseja calcular o fatorial: "))

if n < 0:
    print("digite um número positivo ou igual a zero")
elif n == 0:
    fat = 1
else: 
    fat = n
    i = n - 1
    while i >= 2:
        fat = fat * i
        i = i - 1

print(fat)