import pygame
import variaveis_interface as int_vars
from loop_controle import loop_relogio
# funcs
from uso_memoria import mostra_uso_memoria
from uso_cpu import mostra_uso_cpu
from uso_disco import mostra_uso_disco

# Iniciando tela
pygame.display.set_caption("Gerenciamento computador")
pygame.display.init()

# Chamada das funcoes:
def chama_funcs():
    mostra_uso_cpu()
    mostra_uso_memoria()
    mostra_uso_disco()

loop_relogio(chama_funcs)

pygame.display.quit()