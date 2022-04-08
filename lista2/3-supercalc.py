'''
Este programa introduz o conceito de função e procedimento em Python.
Implementa uma calculadora que pode ser acessada através de um menu.
O usuário escolhe a operação através do menu, sendo elas listadas na 
variável menu abaixo:
'''

menu = """
Escolha dentre as operações abaixo e digite os operandos, ou digite 'sai' pra sair:
som: soma
sub: subtração
div: divisão
mul: multiplicação
Digite a sigla da operação: 
"""

'''
nós também definimos uma função em Python:
ela recebe três parâmetros e retorna o resultado da operação.
caso o usuário digite uma sigla que não corresponde a nenhuma 
operação existente, uma exceção é jogada indicando o erro.
'''
def calcula(op, x, y):
    match op:
        case 'som':
            soma = x + y
            return soma
        case 'sub':
            return x - y
        case 'mul':
            mult = x * y
            return mult
        case 'div':
            return x / y
        case _:
            raise ValueError("Operação inválida")

            
# início do programa principal
fim = False
while not fim:
    cmd = input(menu)
    if cmd == 'sai':
        print("Saindo do programa... Tchau!")
        fim = True
    else:
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        try:
            resultado = calcula(cmd, a, b)
            print(resultado)
        except ValueError as e:
            print(e)
