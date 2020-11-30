import psutil
import cpuinfo
import pygame

from info_cpu import mostra_info_cpu
import variaveis_interface as int_vars

#vars
surface1 = int_vars.s1
surface2 = int_vars.s2
lista_percentual_cpus = psutil.cpu_percent(1, percpu=True)

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
    pygame.draw.rect(surface1, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(surface1, int_vars.VERMELHO, (20, 50, larg, 70))
    texto_barra = "Uso de CPU (Total: " + str(capacidade) + "%):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface1, (0, 0))  # setando divisao tela
    int_vars.tela.blit(text, (20, 10))

def mostra_uso_de_cada_cpu(s, l_cpu_percent):
    s.fill(int_vars.CINZA)
    int_vars.tela.blit(s, (0, int_vars.tela_altura / 3))

    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = int_vars.tela_altura / 3
    larg = (s.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(s, int_vars.VERMELHO, (d, y, larg, alt))
        pygame.draw.rect(s, int_vars.AZUL, (d, y, larg, (1 - i / 100) * int_vars.tela_altura/3))
        d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    int_vars.tela.blit(s, (0, int_vars.tela_altura / 4))


def cpu_tela():
    mostra_uso_cpu()
    mostra_uso_de_cada_cpu(surface2, lista_percentual_cpus)
    mostra_info_cpu()
