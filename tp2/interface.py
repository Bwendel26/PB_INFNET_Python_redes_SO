import pygame
import psutil
from uso_memoria import mostra_uso_memoria
from loop_controle import loop_relogio
from variaveis_interface import *

# Iniciando tela
pygame.display.set_caption("Gerenciamento computador")
pygame.display.init()

# Chamada das funcoes:
loop_relogio(mostra_uso_memoria)

pygame.display.quit()