import pygame

AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
dimensoes = [800, 600]

#Iniciando tela
tela_largura = dimensoes[0]
tela_altura = dimensoes[1]
tela = pygame.display.set_mode((tela_largura, tela_altura))
# fonte
pygame.font.init()
font = pygame.font.Font(None, 32)
