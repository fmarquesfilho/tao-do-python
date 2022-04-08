'''
O programa abaixo define uma função chamada de par. Esta função retorna verdadeiro quando o número é par 
e falso quando o número é ímpar.
'''
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))
if par(numero):
    print("o número digitado é par.")
else:
    print("o número digitado é ímpar.")
