
def fatorial(n):
    if n == 0:
        fat = 1
    else: 
        fat = n
        i = n - 1
        while i >= 2:
            fat = fat * i
            i = i - 1
    return fat

def superfatorial(n):
    superfat = 1
    i = n
    while i > 1:
        superfat = superfat * fatorial(i)
        i = i - 1
    return superfat

# início do programa
menu = '''
Digite o número inteiro positivo para o qual deseja calcular o superfatorial 
ou 's' para sair: 
'''
fim = False
while not fim:
    entrada = input(menu)
    if entrada == "s":
        fim = True
    else: 
        n = int(entrada)
        if n >= 0:
            resultado = superfatorial(n)
            print("O superfatorial de {} é {}.".format(n, resultado))
        else:
            print("não existe o fatorial de números negativos.")

