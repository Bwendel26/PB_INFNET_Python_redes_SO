import psutil
import platform
import variaveis_interface as int_vars
import pygame
import cpuinfo

info = cpuinfo.get_cpu_info()


surface2 = int_vars.s2

def mostra_texto(s1, nome, chave, pos_y):

    text = int_vars.font.render(nome, True, int_vars.PRETO)
    s1.blit(text, (10, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        s = str(info[chave])
    text = int_vars.font.render(s, True, int_vars.CINZA)
    s1.blit(text, (200, pos_y))

def mostra_info_cpu():

    # Mostra as informações de CPU escolhidas:
    surface2.fill(int_vars.BRANCO)
    mostra_texto(surface2, "Nome:", "bits", 10)
    mostra_texto(surface2, "Arquitetura:", "arch", 30)
    mostra_texto(surface2, "Palavra (bits):", "bits", 50)
    mostra_texto(surface2, "Frequência (MHz):", "freq", 70)
    mostra_texto(surface2, "Núcleos (físicos):", "nucleos", 90)
    int_vars.tela.blit(surface2, (0, int_vars.tela_altura / 4))