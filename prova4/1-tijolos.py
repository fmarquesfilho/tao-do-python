'''
Implemente a função desenha_tijolo(lh) para que ela desenhe um tijolo com largura
na horizontal 'lh', cujo valor é informado pelo usuário.

*** Não modifique nenhuma outra parte do código abaixo, apenas a função desenha_tijolo(lh).

A função de desenhar tijolos é por sua vez usada pela função desenha_pilha(h),
que está pronta. Seu trabalho é de implementar APENAS a função desenha_tijolo(lh) 
para que ela desenhe cada tijolo da pilha. Pilhas tem altura 'h', outro parâmetro
informado pelo usuário como entrada no programa.

Exemplo de execução:

Digite a altura da pilha de tijolos: 2
Digite a largura horizontal de cada tijolo: 9
=========
=       =
=========
=========
=       =
=========
(fim de execução)

(*) acima uma pilha com 2 tijolos, isto é, altura 'h' igual a 2
(**) acima cada tijolo tem uma largura na horizontal 'lh' igual a 9

O usuário informa o número 'h' de tijolos que será empilhado, bem como a largura 
na horizontal 'lh' de cada tijolo, que no caso do exemplo acima é 9 (nove), 
pois equivale ao número de caracteres do tipo '=' (igual) na horizontal.

Note que a largura horizontal 'lh' não pode ser inferior a 3, 
e a altura 'h' não pode ser inferior a 1. 

Abaixo um exemplo de execução com o menor tijolo possível e a menor 
pilha possível (apenas 1 tijolo):

Digite a altura da pilha de tijolos: 1
Digite a largura horizontal de cada tijolo: 3
===
= =
===
(fim de execução)
'''

def desenha_tijolo(lh):
    # >>>>>>>>>>>>>>>>
    # modificar abaixo
    # >>>>>>>>>>>>>>>>

    print("=")
    
    # <<<<<<<<<<<<<<<
    # modificar acima
    # <<<<<<<<<<<<<<<


def desenha_pilha(h, lh):
    i = 0
    while i < h:
        desenha_tijolo(lh)
        i = i + 1


# programa principal
h = int(input("Digite a altura da pilha de tijolos: "))
if h < 1:
    print("Altura da pilha de tijolos não pode ser inferior a 1.")
else:
    lh = int(input("Digite a largura horizontal de cada tijolo: "))
    if lh < 3:
        print("A largura horizontal do tijolo não pode ser inferior a 3.")
    else:
        desenha_pilha(h, lh)
