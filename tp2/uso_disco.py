import psutil
import pygame
import variaveis_interface as int_vars

surface3 = int_vars.s3

def mostra_uso_disco():
    # disk = str(disk)
    disco = psutil.disk_usage('./')
    larg = int_vars.tela_largura - 2 * 20
    int_vars.tela.fill(int_vars.PRETO)
    pygame.draw.rect(surface3, int_vars.AZUL, (20, 50, larg, 70))
    larg = larg * disco.percent / 100
    pygame.draw.rect(surface3, int_vars.VERMELHO, (20, 50, larg, 70))
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface3, (0, 2*int_vars.tela_altura/4)) #setando divisao tela
    int_vars.tela.blit(text, (20, 2*int_vars.tela_altura/4)) # setando posicao do text

# print(psutil.disk_partitions())
# Modificar para iterar sobre cada disco do pc
# e consequentemente criar uma surface para cada um.