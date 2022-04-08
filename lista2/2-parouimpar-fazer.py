'''
Baseado no exercício anterior, modifique o programa abaixo para que ele faça o que é esperado.
'''
def impar(n):
    # implemente a função, por enquanto ela retorna verdadeiro 
    # independente do número passado a ela (isso está errado!)
    # escreva o seu código aqui para que a função tenha o
    # comportamento esperado, que é retornar verdadeiro quando
    # o número passado é ímpar, e falso quando é par
    return True

# não é pra mexer no código abaixo
numero = int(input("Digite um número inteiro: "))
if impar(numero):
    print("o número digitado é ímpar.")
else:
    print("o número digitado é par.")
