'''
Uma lavadoura de roupas é controlada pelo programa abaixo.
Sua tarefa nesta prova é modificar a função "iniciar" deste programa. 

O LOCAL QUE VOCÊ PODE MODIFICAR ESTÁ INDICADO COM COMENTÁRIO
NÃO MODIFIQUE NENHUMA OUTRA PARTE DESTE PROGRAMA ALÉM DA FUNÇÃO INICIAR
LEIA ATENTAMENTE O ENUNCIADO ABAIXO ANTES DE COMEÇAR A PROGRAMAR
SE HOUVER DÚVIDAS ME PROCURE NO DISCORD COM MENSAGEM PRIVADA, 
EU FICAREI APENAS NO INÍCIO DA PROVA NA SALA DO GOOGLE MEET

A lavadora oferece três tipos de lavagens:
1- lavagem leve (não executa a etapa de molho. inicia na etapa de lavagem, 
depois vai para o enxague e finalmente para a centrifugação)
2- lavagem normal (passa por todas as etapas, do molho a centrifugação)
3- enxágue duplo (faz o mesmo que a lavagem normal, mas realiza o enxágue duas vezes)

Da maneira que está, a função "iniciar" só está ajustando o nível de água 
antes de iniciar a lavagem, nada mais do que isto. 
Você precisa modificar a função "iniciar" para que ela execute as demais etapas da lavagem, 
de acordo com o programa escolhido pelo usuário.

Cada estágio da lavagem possui uma função correspondente que pode ou não ser chamada, 
dependendo do programa de lavagem escolhido. Lembrando que as etapas de lavagem 
precisam estar em ordem: o molho vem antes da lavagem, que por sua vez vem antes 
do enxágue, que vem antes da centrifugação.

As funções disponíveis são "molho", "lavagem", "enxague" e "centrifugacao". 
Mais uma vez, não modifique nada nessas funções auxiliares, elas já estão prontas.
O mesmo vale para o restante do programa, modifique APENAS onde está indicado (ver abaixo).
Qualquer solução contendo modificação fora do lugar indicado será desconsiderada.

OBSERVAÇÃO: no código abaixo eu uso um recurso do Python que não comentei em aula 
chamado de "global". Basicamente o "global" na frente do nome de uma variável torna acessível 
uma variável que foi declarada fora da própria função. 

Lembra que eu disse em aula que as variáveis no código de uma função são
por padrão de escopo local a função? Isso quer dizer que as variáveis passadas por 
parâmetro da função, bem como aquelas criadas dentro da função, são acessíveis somente
ao código da função em si. Por padrão, uma função não tem acesso às variáveis que foram 
declaradas fora dela, a menos que a gente use a palavra reservada "global". Isso permite 
que a função acesse e modifique o valor de variáveis que foram declaradas fora da 
própria função. No caso do código abaixo, eu uso variáveis globais para guardar o estado  
atual da lavagem (molho, lavagem, enxágue ou centrifugação). Cada função implementada 
pode modificar esse estado, por isso eu uso global para tornar acessível para cada função 
a variável que controla em qual estágio a lavagem se encontra.

Exemplo:

### Menu da Lavadora ###
Selecione o programa de lavagem ou 0 (zero) para desligar:
1- lavagem leve (elimina a etapa de molho e inicia na lavagem até a centrifugação)
2- lavagem normal (passa por todas as etapas, do molho a centrifugação)
3- enxágue duplo (faz o mesmo que a lavagem normal, mas realiza o enxágue duas vezes)

Digite o programa desejado para essa lavagem: 1

Selecione o nível de água ou 0 (zero) para desligar:
1- pouca roupa
2- dia a dia
3- tanque cheio

Digite o nível de água desejado para essa lavagem: 2
Nível atual: 0. Novo nível: 2. Enchendo a lavadora...
Iniciando...
Entrando no estágio 2 (lavagem)...
Entrando no estágio 3 (enxágue)...
Entrando no estágio 4 (centrifugação)...
Finalizando a lavagem...

>>>>>>>>>>>>>>>>
ÍNICIO DO CÓDIGO
>>>>>>>>>>>>>>>>
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
# note que a função só modifica a variável nivel_atual caso o nível passado como
# parâmetro seja MAIOR que o nível atual
def encher(nivel):
    global nivel_atual
    if nivel > nivel_atual:
        print("Nível atual: {}. Novo nível: {}. Enchendo a lavadora...".format(nivel_atual, nivel))
        nivel_atual = nivel

# esvazia o tanque da lavadora até o nível de água passado como parâmetro da função
# note que a função só modifica a variável nivel_atual caso o nível passado como
# parâmetro seja MENOR que o nível atual
def esvaziar(nivel):
    global nivel_atual
    if nivel < nivel_atual:
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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# MODIFIQUE APENAS A FUNÇÃO ABAIXO NO LOCAL INDICADO
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A função INICIAR abaixo tem duas responsabilidades:
# 1- corrigir o nível de água de lavadora se necessário (ISTO JÁ ESTÁ FEITO, NÃO MODIFIQUE!)
# 2- executar cada estágio de lavagem de acordo com o programa escolhido (ISTO VOCÊ PRECISA FAZER)
def iniciar(programa, nivel):
    global nivel_atual

    # ajusta o nível da água se necessário antes de começar de fato a programação
    if nivel_atual > nivel:
        esvaziar(nivel)
    elif nivel_atual < nivel:
        encher(nivel)

    print("Iniciando a lavagem...")
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # escrever AQUI o código que muda os estágios de lavagem de acordo  
    # com o programa passado como parâmetro desta função
    # MODIFIQUE APENAS ESSA PARTE DO CÓDIGO
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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
    