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

s1 = pygame.surface.Surface((int_vars.tela_largura, int_vars.tela_altura / 4))
s2 = pygame.surface.Surface((int_vars.tela_largura, int_vars.tela_altura / 4))
s3 = pygame.surface.Surface((int_vars.tela_largura, int_vars.tela_altura / 4))
s4 = pygame.surface.Surface((int_vars.tela_largura, int_vars.tela_altura / 8))
s5 = pygame.surface.Surface((int_vars.tela_largura, int_vars.tela_altura / 8))

# Chamada das funcoes:
loop_relogio(s1, mostra_uso_cpu)
loop_relogio(s2, mostra_uso_memoria)
loop_relogio(s3, mostra_uso_disco)

pygame.display.quit()