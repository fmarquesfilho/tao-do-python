'''
O programa abaixo calcula o superfatorial de um número inteiro 
fornecido pelo usuário. 
A função superfatorial recebe como parâmetro o número para o qual
deseja-se calcular o superfatorial e retorna o resultado do cálculo.
O seu trabalho é implementar a função superfatorial para que ela
retorne o resultado correto. (4,0 pontos)

NÃO MODIFIQUE O RESTANTE DO PROGRAMA,
APENAS A FUNÇÃO SUPERFATORIAL ABAIXO.

Note que a função fatorial já está implementada para calcular o fatorial
de um número inteiro maior ou igual a zero. Você deve fazer uso dessa
função na sua solução.

O que é um superfatorial? 

O superfatorial é definido como o produto dos primeiros 'n' fatoriais.
Assim, o superfatorial de 4 é:
1! x 2! x 3! x 4! = 288 

Exemplo de execução:

Digite o número inteiro positivo para o qual deseja calcular o superfatorial 
ou 's' para sair: 
4
O superfatorial de 4 é 288.

Digite o número inteiro positivo para o qual deseja calcular o superfatorial 
ou 's' para sair: 
1
O superfatorial de 1 é 1.

Digite o número inteiro positivo para o qual deseja calcular o superfatorial 
ou 's' para sair: 
3
O superfatorial de 3 é 12.
'''

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
    # escreva a sua solução aqui e não modifique outra parte do programa
    return 0


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
