'''
Esta é a solução que eu fiz para o problema da lavadora que caiu na segunda prova,
e também na terceira lista.
Após análise, observa-se que a solução da terceira lista (código incluso abaixo):
1- muda os estágios da lavadora da forma correta, mas não esvazia o tanque para 
o nível 0 (zero) de água durante a troca dos estágios.
2- observou-se que a solução tenta esvaziar o tanque do estágio de molho para
o estágio de lavagem. isso causa desperdício de água.

Modifique o programa abaixo para que:

1- a máquina esvazie para o nível 0 (zero) e encha o tanque com água limpa 
ao término de cada estágio (1,5 ponto). 
2- a máquina NÃO faça a troca da água do tanque do estágio molho para lavagem, 
utilizando a mesma água tanto no estágio molho quanto na lavagem (veja no
exemplo de execução abaixo que não há esvaziamento do tanque da lavadora dos
estágios 1 para 2) - (1,5 ponto).

As modificações devem ser feitas APENAS na função iniciar no trecho indicado abaixo
com comentário. 

*** NÃO MODIFIQUE NENHUMA OUTRA PARTE DO PROGRAMA, APENAS O TRECHO INDICADO ***

Compare a saída atual do programa com a saída esperada. Qualquer alteração fora 
do local indicado resultará na não aceitaçào da solução e consequentemente zero no exercício.

Exemplo de execução:

### Menu da Lavadora ###
Selecione o programa de lavagem ou 0 (zero) para desligar:
1- lavagem leve (elimina a etapa de molho e inicia na lavagem até a centrifugação)
2- lavagem normal (passa por todas as etapas, do molho a centrifugação)
3- enxágue duplo (faz o mesmo que a lavagem normal, mas realiza o enxágue duas vezes)

Digite o programa desejado para essa lavagem: 2

Selecione o nível de água ou 0 (zero) para desligar:
1- pouca roupa
2- dia a dia
3- tanque cheio

Digite o nível de água desejado para essa lavagem: 2
Nível atual: 0. Novo nível: 2. Enchendo a lavadora...
Iniciando...
Entrando no estágio 1 (de molho)...
Entrando no estágio 2 (lavagem)...
Nível atual: 2. Novo nível: 0. Esvaziando a lavadora...
Nível atual: 0. Novo nível: 2. Enchendo a lavadora...
Entrando no estágio 3 (enxágue)...
Nível atual: 2. Novo nível: 0. Esvaziando a lavadora...
Entrando no estágio 4 (centrifugação)...
Finalizando a lavagem...
'''

# nível de água da lavadora
# 0- tanque vazio
# 1- tanque com pouca água (pouca roupa)
# 2- tanque com nível médio de água
# 3- tanque cheio
nivel_atual = 0

# estágio da lavagem
# 0- desligada
# 1- molho
# 2- lavagem
# 3- enxague
# 4- centrifugação
estagio_atual = 0

# enche o tanque da lavadora até o nível de água passado como parâmetro da função
def encher(nivel):
    global nivel_atual
    print("Nível atual: {}. Novo nível: {}. Enchendo a lavadora...".format(nivel_atual, nivel))
    nivel_atual = nivel

# esvazia o tanque da lavadora até o nível de água passado como parâmetro da função
def esvaziar(nivel):
    global nivel_atual
    print("Nível atual: {}. Novo nível: {}. Esvaziando a lavadora...".format(nivel_atual, nivel))
    nivel_atual = nivel

# as quatro funções abaixo modificam a variável estagio_atual que corresponde 
# ao estágio atual da lavagem
def molho():
    global estagio_atual
    if estagio_atual > 1:
        print("Lavadora no estágio {}. Não é possível retornar para um estágio anterior.".format(estagio_atual))
    else:
        estagio_atual = 1
        print("Entrando no estágio 1 (de molho)...")

def lavagem():
    global estagio_atual
    if estagio_atual > 2:
        print("Lavadora no estágio {}. Não é possível retornar para um estágio anterior.".format(estagio_atual))
    else:
        estagio_atual = 2
        print("Entrando no estágio 2 (lavagem)...")

def enxague():
    global estagio_atual
    if estagio_atual > 3:
        print("Lavadora no estágio {}. Não é possível retornar para um estágio anterior.".format(estagio_atual))
    else:
        estagio_atual = 3
        print("Entrando no estágio 3 (enxágue)...")

def centrifugacao():
    global estagio_atual
    if estagio_atual > 4:
        print("Lavadora no estágio {}. Não é possível retornar para um estágio anterior.".format(estagio_atual))
    else:
        estagio_atual = 4
        print("Entrando no estágio 4 (centrifugação)...")

# desliga a lavadora
def desliga():
    global estagio_atual
    if estagio_atual == 0:
        print("Lavadora já está desligada.")
    else:
        estagio_atual = 0
        print("Desligando a lavadora. Bye bye...")


def iniciar(programa, nivel):
    global nivel_atual

    # ajusta o nível da água se necessário antes de começar de fato a programação
    if nivel_atual > nivel:
        esvaziar(nivel)
    elif nivel_atual < nivel:
        encher(nivel)

    print("Iniciando...")

    # >>>>>>>>>>>>>>>>>
    # MODIFIQUE ABAIXO 
    # >>>>>>>>>>>>>>>>>
    if programa == 1:
        # leve, sem molho
        lavagem()
        esvaziar(nivel)
        encher(nivel)
        enxague()
        esvaziar(nivel)
        centrifugacao()
    elif programa == 2:
        # lavagem completa passando por todas as etapas
        molho()
        esvaziar(nivel)
        encher(nivel)
        lavagem()
        esvaziar(nivel)
        encher(nivel)
        enxague()
        esvaziar(nivel)
        centrifugacao()
    elif programa == 3:
        # lavagem completa com duplo enxágue
        molho()
        esvaziar(nivel)
        encher(nivel)
        lavagem()
        esvaziar(nivel)
        encher(nivel)
        enxague()
        esvaziar(nivel)
        encher(nivel)
        enxague()
        esvaziar(nivel)
        centrifugacao()
    # >>>>>>>>>>>>>>>>>
    # MODIFIQUE ACIMA
    # >>>>>>>>>>>>>>>>>

    print("Finalizando a lavagem...")


# menu dos programas de lavagem que é mostrado ao usuário
menu_programa = """
### Menu da Lavadora ###
Selecione o programa de lavagem ou 0 (zero) para desligar:
1- lavagem leve (elimina a etapa de molho e inicia na lavagem até a centrifugação)
2- lavagem normal (passa por todas as etapas, do molho a centrifugação)
3- enxágue duplo (faz o mesmo que a lavagem normal, mas realiza o enxágue duas vezes)
"""

# menu dos níveis de água que é mostrado ao usuário
menu_niveis = """
Selecione o nível de água ou 0 (zero) para desligar:
1- pouca roupa
2- dia a dia
3- tanque cheio
"""

# programa principal
fim = False
while not fim:
    print(menu_programa)
    programa = int(input("Digite o programa desejado para essa lavagem: "))
    if programa == 0:
        fim = True
        desliga()
    elif programa >= 1 and programa <= 3:
        print(menu_niveis)
        nivel = int(input("Digite o nível de água desejado para essa lavagem: "))
        if nivel == 0:
            fim = True
            desliga()
        elif nivel >= 1 and nivel <= 3:
            iniciar(programa, nivel)
        else:
            print("Nível de água inválido.")
    else:
        print("Programa inválido.")
    