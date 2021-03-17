import psutil
import pygame
import variaveis_interface as int_vars

# vars
memoria = psutil.virtual_memory()
surface1 = int_vars.s1


#funcs
def percentual_memoria():
    """
    This funcs use the psutil lib to get the memory
    used percent.
    :return: float percentual_usado
    """

    mem = psutil.virtual_memory().percent
    return mem


def mostra_uso_memoria():
    mem = percentual_memoria()
    larg = int_vars.tela_largura - 2 * 20
    int_vars.tela.fill(int_vars.PRETO)
    pygame.draw.rect(surface1, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg * mem / 100
    pygame.draw.rect(surface1, int_vars.VERMELHO, (20, 50, larg, 70))
    texto_barra = "Uso de Memória (Total: " + str(mem) + "%):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface1, (0, 0))  # setando divisao tela
    int_vars.tela.blit(text, (20, 10))