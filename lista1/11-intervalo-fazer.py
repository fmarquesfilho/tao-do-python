'''
Escreva um programa que lê dois números inteiros x e y que constituem
respectivamente os limites inferior e superior de um intervalo. 
O programa imprime apenas os números inteiros pares existentes no intervalo
entre x e y, incluindo x e y, e ao final imprime quantos pares foram
encontrados no intervalo.
Por exemplo:
Digite o limite inferior: 6
Digite o limite superior: 9
6
8
Foram encontrados 2 números pares no intervalo entre 6 e 9.
< fim de execução >
''' 

x = int(input("Digite o limite inferior: "))
y = int(input("Digite o limite superior: "))

i = x
pares = 0
while i <= y:
    if i % 2 == 0:
        print(i)
        pares = pares + 1
    i = i + 1

print("Foram encontrados {} números pares no intervalo entre {} e {}.".format(pares, x, y))