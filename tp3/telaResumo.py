import psutil
import cpuinfo
import pygame
import platform

import variaveis_interface as int_vars

#CPU
    #vars:
surface1 = int_vars.sr1
surface2 = int_vars.sr2
surface3 = int_vars.sr3
surface4 = int_vars.sr4
surface5 = int_vars.sr5
lista_percentual_cpus = psutil.cpu_percent(1, percpu=True)
percentual_usado = psutil.cpu_percent(interval=0)

    #funcs:
def mostra_uso_cpu():
    capacidade = percentual_usado
    larg = int_vars.tela_largura - 2*20
    pygame.draw.rect(surface2, int_vars.AZUL, (20, 35, larg, 60))
    larg = larg*capacidade/100
    pygame.draw.rect(surface2, int_vars.VERMELHO, (20, 35, larg, 60))
    texto_barra = "Uso de CPU (Total: " + str(capacidade) + "%):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface2, (0, int_vars.tela_altura / 5))  # setando divisao tela
    int_vars.tela.blit(text, (20, int_vars.tela_altura / 5))


info = cpuinfo.get_cpu_info()

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
    int_vars.tela.fill(int_vars.PRETO)
    surface1.fill(int_vars.BRANCO)
    mostra_texto(surface1, "Nome:", "brand_raw", 10)
    mostra_texto(surface1, "Arquitetura:", "arch", 30)
    mostra_texto(surface1, "Palavra (bits):", "bits", 50)
    mostra_texto(surface1, "Frequência (MHz):", "freq", 70)
    mostra_texto(surface1, "Núcleos (físicos):", "nucleos", 90)
    int_vars.tela.blit(surface1, (0, 0))

#MEMORIA

def mostra_uso_memoria():
    mem = psutil.virtual_memory().percent
    larg = int_vars.tela_largura - 2 * 20
    pygame.draw.rect(surface3, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg * mem / 100
    pygame.draw.rect(surface3, int_vars.VERMELHO, (20, 50, larg, 70))
    texto_barra = "Uso de Memória (Total: " + str(mem) + "%):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface3, (0, 2 * int_vars.tela_altura / 5))  # setando divisao tela
    int_vars.tela.blit(text, (20, 2 * int_vars.tela_altura / 5))

#DISCO
def mostra_uso_disco():
    # disk = str(disk)
    disco = psutil.disk_usage('./')
    larg = int_vars.tela_largura - 2 * 20
    pygame.draw.rect(surface4, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg * disco.percent / 100
    pygame.draw.rect(surface4, int_vars.VERMELHO, (20, 50, larg, 70))
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface4, (0, 3 * int_vars.tela_altura / 5)) #setando divisao tela
    int_vars.tela.blit(text, (20, 3 * int_vars.tela_altura / 5)) # setando posicao do text


#MAIN
def main():
    mostra_info_cpu()
    mostra_uso_cpu()
    mostra_uso_memoria()
    mostra_uso_disco()
