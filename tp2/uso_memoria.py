import psutil
import pygame
import variaveis_interface as int_vars
#variaveis
memoria = psutil.virtual_memory()

#funcs
def percentual_memoria():
    """
    Função que retorna o percentual de memoria RAM
    utilizado por um computador.
    :return: float percentual_usado
    """
    total_gb = round((memoria.total/(1024 ** 3)), 3)
    usada_gb = round((memoria.used/(1024 ** 3)), 3)
    percentual_usado = (usada_gb * 100) / total_gb

    return round(percentual_usado, 3)

surface2 = int_vars.s2

def mostra_uso_memoria():
    mem = percentual_memoria()
    larg = int_vars.tela_largura - 2 * 20
    int_vars.tela.fill(int_vars.PRETO)
    pygame.draw.rect(surface2, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg * mem / 100
    pygame.draw.rect(surface2, int_vars.VERMELHO, (20, 50, larg, 70))
    texto_barra = "Uso de Memória (Total: " + str(mem) + "GB):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface2, (0, int_vars.tela_altura / 4))  # setando divisao tela
    int_vars.tela.blit(text, (20, int_vars.tela_altura / 4))