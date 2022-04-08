'''
A iluminação de uma estufa para plantio de verduras é controlada pelo programa abaixo.
Sua tarefa nesta prova é modificar a função "iniciar" deste programa. 

O LOCAL QUE VOCÊ PODE MODIFICAR ESTÁ INDICADO COM COMENTÁRIO
NÃO MODIFIQUE NENHUMA OUTRA PARTE DESTE PROGRAMA ALÉM DA FUNÇÃO INICIAR
LEIA ATENTAMENTE O ENUNCIADO ABAIXO ANTES DE COMEÇAR A PROGRAMAR
SE HOUVER DÚVIDAS ME PROCURE NO DISCORD COM MENSAGEM PRIVADA, 
EU FICAREI APENAS NO INÍCIO DA PROVA NA SALA DO GOOGLE MEET

Você precisa modificar a função "iniciar" (abaixo) para que ela simule um dia completo 
de iluminação solar. O usuário deve informar o período do dia atual e o programa deve 
modificar a potência das lâmpadas até completar 24 horas de iluminação a partir do 
período informado.

A estufa oferece três tipos de iluminação:
0- iluminação desligada
1- iluminação mínima (as lâmpadas funcionam em baixa potência)
2- iluminação normal (as lâmpadas funcionam em potência normal)
3- iluminação máxima (as lâmpadas funcionam em alta potência)

A ordem de acionamento das lâmpadas é a seguinte:
da noite para o nascer do sol (de 0 para 1 - luzes são acesas em potência mínima), 
do nascer do sol para manhã (de 1 para 2 - luzes mudam da potência mínima para normal),
da manhã para o meio dia (de 2 para 3 - luzes mudam da potência normal para máxima),
do meio dia para tarde (de 3 para 2 - luzes mudam da potência máxima para normal),
da tarde para o por do sol (de 2 para 1 - luzes mudam da potência normal para mínima),
do por do sol para noite (de 1 para 0 - luzes são desligadas).

Se o usuário informar 1 (noite), as luzes devem iniciar desligadas, passar para 
potência mínima (nascer do sol), então normal (manhã), máxima (meio dia), depois passar 
para normal (tarde), mínima (por do sol) e finalmente serem desligadas (noite).
Se o usuário informar o período 2 (manhã), as luzes devem iniciar na 
potência normal, passar para máxima (meio dia), depois para normal (tarde), 
por do sol (mínima), então desligar (noite), para então entrar em potência mínima 
(nascer do sol) e voltar para iluminação normal (manhã). 
Se o usuário informar o período 3 (tarde), bem, deixo este pra você pensar.
Vai seguir a mesma lógica dos dois acima.

Cada estágio da iluminação possui uma função correspondente já implementada. 
Lembrando que as etapas de iluminação precisam seguir a ordem acima: o por do sol 
vem antes da manha, que por sua vez vem antes do meio dia, que vem antes da tarde, 
que vem antes do por do sol, que vem antes da noite, que vem antes do por do sol.
 
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
atual do sistema de iluminação (potências mínima, normal, máxima). Cada função implementada 
pode modificar esse estado, por isso eu uso global para tornar acessível para cada função 
a variável que controla o estado do sistema de iluminação.

Exemplo de execução correta do programa:

### Menu de iluminação da estufa ###
Selecione o período ou 0 (zero) para desligar o sistema de iluminação:
1- noite
2- manhã
3- tarde

Digite o período do dia atual: 2
Iniciando o sistema de iluminação...
Entrando no estágio 2 (iluminação em potência normal)...
Entrando no estágio 3 (iluminação em potência máxima)...
Entrando no estágio 2 (iluminação em potência normal)...
Entrando no estágio 1 (iluminação em potência mínima)...
Desligando as luzes. Bons sonhos...
Entrando no estágio 1 (iluminação em potência mínima)...
Entrando no estágio 2 (iluminação em potência normal)...
Terminadas as 24 horas de iluminação da estufa.

>>>>>>>>>>>>>>>>
ÍNICIO DO CÓDIGO
>>>>>>>>>>>>>>>>
'''

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
    print("Entrando no estágio 1 (iluminação em potência mínima)...")

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
        print("As luzes já estão desligadas.")
    else:
        estagio_atual = 0
        print("Desligando as luzes. Bons sonhos...")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# MODIFIQUE APENAS A FUNÇÃO ABAIXO NO LOCAL INDICADO
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A função INICIAR abaixo deve acionar a potência correta
# de iluminação dependendo do horário do dia
def iniciar(periodo):
    global estagio_atual

    print("Iniciando o sistema de iluminação...")
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # escrever AQUI o código que muda os estágios da iluminação de acordo  
    # com o período passado como parâmetro desta função
    # MODIFIQUE APENAS ESSA PARTE DO CÓDIGO
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    print("Terminadas 24 horas de iluminação da estufa.")


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
    
