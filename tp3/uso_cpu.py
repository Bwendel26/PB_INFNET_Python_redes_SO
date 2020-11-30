import psutil
import cpuinfo
import pygame

from info_cpu import mostra_info_cpu
import variaveis_interface as int_vars

#funcs
def percentual_cpu():
    """
    Função que retorna o percentual de uso da CPU
    do computador.
    :param tempo: em segundos para retornar o percentual.
    :return: float percentual_usado
    """
    percentual_usado = psutil.cpu_percent(interval=0)

    return percentual_usado


surface1 = int_vars.s1

def mostra_uso_cpu():
    capacidade = percentual_cpu()
    larg = int_vars.tela_largura - 2*20
    int_vars.tela.fill(int_vars.PRETO)
    pygame.draw.rect(surface1, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(surface1, int_vars.VERMELHO, (20, 50, larg, 70))
    texto_barra = "Uso de CPU (Total: " + str(capacidade) + "%):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface1, (0, 0))  # setando divisao tela
    int_vars.tela.blit(text, (20, 10))


def cpu_tela():
    mostra_uso_cpu()
    mostra_info_cpu()