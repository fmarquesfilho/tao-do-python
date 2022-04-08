
def desenha_tijolo(lh):
    lin = 1       # contador da linha
    lv = 3        # largura do tijolo na vertical
    while lin <= lv:
        col = 1   # contador da coluna
        while col <= lh:
            if lin == 1 or lin == lv or col == 1 or col == lh:
                print("=", end='')  # não quebra a linha
            else:
                print(" ", end='')  # não quebra a linha
            col = col + 1
        print("")
        lin = lin + 1


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
