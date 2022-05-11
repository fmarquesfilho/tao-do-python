'''
Escreva um programa que lê dois números inteiros, 
e imprime uma mensagem caso apenas um dos números
seja ímpar e o outro seja par. O programa não 
deve dizer nada quando ambos foram pares ou
quando ambos forem ímpares.
''' 
# Recebe um número inteiro e retorna verdadeiro caso ele seja par e falso
# quando ele for ímpar.
def par(i):
    r = i % 2
    return r == 0

def impar(i):
    return not par(i)

x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

# as expressões são avaliadas de dentro pra fora
# ou seja, primeiro se avalia par(x) or par(y)
# que só será verdadeira caso pelo menos 1 dos 
# números seja par. Caso seja verdadeiram avalia-se 
# impar(x) or impar(y) qye segue a mesma lógica,
# sendo verdadeira quando pelo menos 1 dos números
# seja ímpar. Dessa forma conseguimos fazer exatamente
# o que foi pedido no enunciado, ou seja, imprimimos
# apenas quando um número é par e o outro é ímpar.
 
if (par(x) or par(y)) and (impar(x) or impar(y)):
    print("um número é ímpar e o outro é par.")

