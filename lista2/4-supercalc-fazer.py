'''
Baseado no exercício anterior, inclua mais duas operações no programa abaixo, exponenciação e divisão inteira.
'''

# a variável menu já inclui as operações
menu = """
Escolha dentre as operações abaixo e digite os operandos, ou digite 'sai' pra sair:
som: soma
sub: subtração
div: divisão
mul: multiplicação
exp: exponenciação
dii: divisão inteira
Digite a sigla da operação: 
"""

def calcula(cmd, a, b):
    match cmd:
        case 'som':
            return a + b
        case 'sub':
            return a - b
        case 'mul':
            return a * b
        case 'div':
            return a / b
        # adicione as operações aqui
        case 'exp':
            return a ** b
        case 'dii':
            return a // b
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
            print(calcula(cmd, a, b))
        except ValueError as e:
            print(e)
