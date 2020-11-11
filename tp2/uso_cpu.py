import psutil
import pygame
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

def mostra_uso_cpu():
    capacidade = percentual_cpu()
    larg = int_vars.tela_largura - 2*20
    int_vars.tela.fill(int_vars.PRETO)
    pygame.draw.rect(int_vars.tela, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(int_vars.tela, int_vars.VERMELHO, (20, 50, larg, 70))
    texto_barra = "Uso de CPU (Total: " + str(capacidade) + "%):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(text, (20, 10))