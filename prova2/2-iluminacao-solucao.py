# estágio da iluminação
# 0- desligada
# 1- mínima
# 2- normal
# 3- máxima
estagio_atual = 0

# as quatro funções abaixo modificam a variável estagio_atual que corresponde 
# ao estágio atual da iluminação
def minima():
    global estagio_atual
    estagio_atual = 1
    print("Entrando no estágio {} (iluminação em potência mínima)...".format(estagio_atual))

def normal():
    global estagio_atual
    estagio_atual = 2
    print("Entrando no estágio 2 (iluminação em potência normal)...")

def maxima():
    global estagio_atual
    estagio_atual = 3
    print("Entrando no estágio 3 (iluminação em potência máxima)...")

# desliga as luzes
def desliga():
    global estagio_atual
    if estagio_atual == 0:
        print("Luzes já estão desligadas. Durma bem...")
    else:
        estagio_atual = 0
        print("Desligando as luzes. Bons sonhos...")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# MODIFIQUE APENAS A FUNÇÃO ABAIXO NO LOCAL INDICADO
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A função INICIAR abaixo deve acionar a potência correta
# de iluminação dependendo do horário do dia
def iniciar(periodo):
    #global estagio_atual
    print("Iniciando o sistema de iluminação...")
    if periodo == 1:
        desliga() # noite
        minima() # nascer do sol
        #print("Valor atual da variável é ", estagio_atual)
        normal() # manhã
        maxima() # meio dia
        normal() # tarde
        minima() # por do sol
        desliga() # noite do dia seguinte
    elif periodo == 2:
        normal() # tarde
        maxima() # meio dia
        normal() # tarde
        minima() # por do sol
        desliga() # noite
        minima() # nascer do sol
        normal() # manhã do dia seguinte
    elif periodo == 3:
        normal() # tarde
        minima() # por do sol
        desliga() # noite
        minima() # nascer do sol
        normal() # manhã
        maxima() # meio dia
        normal() # tarde do dia seguinte
    print("Terminadas as 24 horas de iluminação da estufa.")


# menu dos períodos que podem ser escolhidos pelo usuário
menu = """
### Menu de iluminação da estufa ###
Selecione o período ou 0 (zero) para desligar o sistema de iluminação:
1- noite
2- manhã
3- tarde
"""

# programa principal
fim = False
while not fim:
    print(menu)
    periodo = int(input("Digite o período do dia atual: "))
    if periodo == 0:
        fim = True
        desliga()
    elif periodo >= 1 and periodo <= 3:
        iniciar(periodo)
    else:
        print("Período inválido.")
    