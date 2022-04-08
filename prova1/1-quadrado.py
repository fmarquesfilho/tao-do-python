'''
O programa abaixo desenha um quadrado usando o número 0 (zero).
O programa recebe como entrada o comprimento do lado, sendo esse comprimento
o número de zeros de cada lado do quadrado. 
O menor quadrado que pode ser desenhado com pelo menos 1 zero de preenchimento 
(dentro do quadrado) é aquele com três zeros, como no exemplo
de execução abaixo:

Digite o tamanho do lado do quadrado: 3
000
000
000

Da maneira que está, o programa está preenchendo todo o interior do quadrado 
com zeros. Modifique o programa para que o interior do quadrado seja vazio 
(valendo 4,0 pontos).

Exemplo com o menor quadrado possível:

Digite o tamanho do lado do quadrado: 3
000
0 0
000
< fim de execução >

Exemplo de quadrado com lado de tamanho 6

Digite o tamanho do lado do quadrado: 6
000000
0    0
0    0
0    0
0    0
000000
< fim de execução >
'''

l = int(input("Digite o tamanho do lado do quadrado: "))
if l >= 3:
    i = 0
    while i < l:
        j = 0
        while j < l:
            # escreve uma linha de zeros
            print("0", end="")
            j = j + 1
        print("") # insere uma quebra de linha
        i = i + 1
else:
    print("Eu apenas desenho quadrados com lado maior ou igual a 3.")