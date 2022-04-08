'''
O programa abaixo recebe do usuário o tempo que uma lasanha já ficou no forno. 
O programa responde quanto tempo a lasanha ainda deve ficar no forno para ficar pronta.
'''

# define a constante 'TEMPO_COZIMENTO' que é o tempo esperado
# de cozimento para a lasanha
TEMPO_COZIMENTO = 40

def tempo_cozimento_restante(tempo_cozimento_gasto):
    return TEMPO_COZIMENTO - tempo_cozimento_gasto


# programa principal
tempo_gasto = int(input("Digite a quantos minutos a lasanha já está no forno: "))
minutos_restantes = tempo_cozimento_restante(tempo_gasto)
print("É esperado que ainda leve {} minutos pra lasanha ficar pronta.".format(minutos_restantes))
