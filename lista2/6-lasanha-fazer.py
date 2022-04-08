'''
Modifique o programa anterior para que ele imprima também o tempo total gasto,
incluindo a preparação da lasanha (2 minutos por camada) somado ao tempo que
a lasanha está no forno. Para isso implemente as funções abaixo.
'''

# define a constante 'TEMPO_COZIMENTO' que é o tempo esperado
# de cozimento para a lasanha
# define a constante 'TEMPO_PREPARACAO' que é igual ao
# tempo usado para preparar uma camada da lasanha
TEMPO_COZIMENTO = 40
TEMPO_PREPARACAO = 2

def tempo_cozimento_restante(tempo_cozimento_gasto):
    return TEMPO_COZIMENTO - tempo_cozimento_gasto

def tempo_preparacao(camadas):
    return TEMPO_PREPARACAO * camadas
    
def tempo_total_gasto(camadas, tempo_gasto):
    return tempo_preparacao(camadas) + tempo_gasto

# programa principal
camadas = int(input("Digite o número de camadas da lasanha (cada camada leva 2 minutos pra ser preparada): "))
tempo_gasto = int(input("Digite a quantos minutos a lasanha já está no forno: "))
print("É esperado que ainda leve {} minutos pra lasanha ficar pronta.".format(tempo_cozimento_restante(tempo_gasto)))
tempo_total = tempo_total_gasto(camadas, tempo_gasto)
print("O tempo total gasto até agora foi de {} minutos.".format(tempo_total))

