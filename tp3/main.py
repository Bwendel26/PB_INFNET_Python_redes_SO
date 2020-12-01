import pygame
from loop_controle import loop_relogio

import variaveis_interface as int_vars
# funcs
from uso_memoria import mostra_uso_memoria
from uso_cpu import cpu_tela
from uso_disco import mostra_uso_disco
from telaResumo import main

# Iniciando tela
pygame.display.set_caption("Gerenciamento computador")
pygame.display.init()
int_vars.tela.fill(int_vars.PRETO)

loop_relogio([cpu_tela, mostra_uso_memoria, mostra_uso_disco], main)

pygame.display.quit()