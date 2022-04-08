def duplofatorial(n):
    if n == 0:
        fat = 1
    else: 
        fat = n
        i = n - 2
        while i >= 2:
            fat = fat * i
            i = i - 2
    return fat

# início do programa
menu = '''
Digite o número inteiro positivo para o qual deseja calcular o duplo fatorial 
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
            resultado = duplofatorial(n)
            print("{}!! = {}.".format(n, resultado))
        else:
            print("não existe o fatorial de números negativos.")

