import pygame
from loop_controle import loop_relogio
# funcs
from uso_memoria import mostra_uso_memoria
from uso_cpu import mostra_uso_cpu
from uso_disco import mostra_uso_disco
from info_cpu import mostra_info_cpu
from info_ip import mostra_info_ip
import variaveis_interface as int_vars

# Iniciando tela
pygame.display.set_caption("Gerenciamento computador")
pygame.display.init()
int_vars.tela.fill(int_vars.PRETO)

loop_relogio([mostra_uso_cpu, mostra_uso_memoria, mostra_uso_disco, mostra_info_cpu, mostra_info_ip])

pygame.display.quit()