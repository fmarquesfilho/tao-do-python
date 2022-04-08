
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


def desenha_camada(lh, x):
    lin = 1       # contador da linha
    lv = 3        # largura do tijolo na vertical
    while lin <= lv:
        col = 1   # contador da coluna
        while col <= lh * x:
            if lin == 1 or lin == lv or col % lh == 1 or col % lh == 0:
                print("=", end='')  # não quebra a linha
            else:
                print(" ", end='')  # não quebra a linha
            col = col + 1
        print("")
        lin = lin + 1


def desenha_parede(h, lh, x):
    i = 0
    while i < h:
        desenha_camada(lh, x)
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
        x = int(input("Digite o número de tijolos na dimensão horizontal da parede (mínimo 1 e máximo 10): "))
        if x < 1 or x > 10:
            print("Parede só pode ter de 1 a 10 tijolos na dimensão horizontal.")
        else:
            desenha_parede(h, lh, x)
