'''
Escreva um programa que lê dois números inteiros x e y que constituem
respectivamente os limites inferior e superior de um intervalo. 
O programa imprime todos os números inteiros existentes no intervalo
entre x e y, excluindo x e y.
Por exemplo:
Digite o limite inferior: 5
Digite o limite superior: 10
6
7
8
9
< fim de execução >
''' 

x = int(input("Digite o limite inferior: "))
y = int(input("Digite o limite superior: "))

i = x + 1
while i < y:
    print(i)
    i = i + 1