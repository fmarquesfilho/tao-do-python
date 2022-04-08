'''
O programa do exercício anterior determina se um número digitado pelo usuário é ou
não é primo. Otimize a sua solução para que o programa realize no pior caso N/2 
operações de divisão para determinar que o número informado pelo usuário é primo.
'''

x = int(input("digite um número inteiro: "))
eh_primo = True

div = 2
while div <= x // 2 and eh_primo:
    if x % div == 0:
        eh_primo = False
    div = div + 1

if eh_primo:
    print("{} é primo.".format(x))
else:
    print("{} não é primo.".format(x))
