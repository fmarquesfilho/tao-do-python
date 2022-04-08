'''
O programa abaixo calcula o duplo fatorial de um número inteiro 
fornecido pelo usuário. 
A função duplofatorial recebe como parâmetro o número para o qual
deseja-se calcular o duplo fatorial e retorna o resultado do cálculo.
O seu trabalho é implementar a função duplofatorial para que ela
retorne o resultado correto. (3,0 pontos)

NÃO MODIFIQUE O RESTANTE DO PROGRAMA,
APENAS A FUNÇÃO DUPLOFATORIAL ABAIXO.

O que é um duplo fatorial? 

O duplo fatorial de um número inteiro par 'n' é definido pela multiplicação
de todos os inteiros pares menores ou iguais a 'n' e maiores ou iguais a 2. 
Por exemplo:
6!! = 6 . 4 . 2 = 48

De forma análoga, o duplo fatorial de um número inteiro ímpar 'n' é definido
pela multiplicação de todos os inteiros ímpares menores ou iguais a 'n' e 
maiores ou iguais a 1.
7!! = 7 . 5 . 3 . 1 = 105

Assim como no fatorial comum, não existe o duplo fatorial de números negativos 
e o duplo fatorial de 0 (zero) é 1.
0!! = 1

Exemplo de execução:

Digite o número inteiro positivo para o qual deseja calcular o fatorial 
ou 's' para sair: 
9
9!! = 945.

Digite o número inteiro positivo para o qual deseja calcular o fatorial 
ou 's' para sair: 
8
8!! = 384.
'''

def duplofatorial(n):
    # escreva a sua solução aqui e não modifique outra parte do programa
    return 0

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

