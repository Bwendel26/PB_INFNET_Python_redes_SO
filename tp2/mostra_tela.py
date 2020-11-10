import pygame

def tela_pygame(largura=800, altura=600):
    #Iniciando tela
    tela_largura = largura
    tela_altura = altura
    tela = pygame.display.set_mode((tela_largura, tela_altura))
    pygame.display.set_caption("Gerenciamento computador")
    pygame.display.init()

    clock = pygame.time.Clock()

    terminou = False
    while not terminou:
        #checar eventos do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            #atualiza a tela
            pygame.display.update()
            # 60 frames p/ seg
            clock.tick(60)

    #finalizando janela
    pygame.display.quit()
    return [tela_largura, tela_altura]