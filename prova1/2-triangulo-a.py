'''
O programa abaixo desenha um triângulo usando o número 0 (zero).
O programa recebe como entrada o tamanho da base, sendo esse comprimento
o número de zeros na base do triângulo. 
O menor triângulo que pode ser desenhado com pelo menos 1 zero dentro dele
é aquele com base que tenha 5 zeros, como no exemplo de execução abaixo:

Digite o tamanho da base do triângulo: 5
  0
 000
00000

Da maneira que está, o programa abaixo está preenchendo todo o interior 
do triângulo com zeros.
Valendo 5,0 pontos, modifique o programa para que ele deixe o interior do 
triângulo vazio, como no exemplo de execução abaixo.  

Digite o tamanho da base do triângulo: 5
  0
 0 0
00000
< fim de execução >

Abaixo, outro exemplo de execução, agora com base 7.

Digite o tamanho da base do triângulo: 7
   0
  0 0
 0   0
0000000
< fim de execução >
'''

b = int(input("Digite o tamanho da base do triângulo: "))
# base precisa ser um número ímpar
impar = (b % 2) == 1 

if b >= 5 and impar:
    h = (b // 2) + 1 # altura do triângulo
    linha = 0 # contador de linhas
    zeros = 1 # contador de zeros
    espacos = b // 2 # contador de espaços
    while linha < h:
        # imprime os espaços na linha
        i = 0
        while i < espacos:
            print(" ", end="")
            i = i + 1

        # imprime os zeros na linha
        i = 0
        while i < zeros:
            print("0", end="")
            i = i + 1

        # prepara para próxima iteração
        print("") # quebra de linha
        zeros = zeros + 2
        espacos = espacos - 1
        linha = linha + 1
else:
    print("Eu apenas desenho triângulos cuja base é um número ímpar maior ou igual a 5.")