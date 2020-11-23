import pygame

def loop_relogio(funcoes):
    # cria relogio
    clock = pygame.time.Clock()
    cont = 60

    terminou = False
    while not terminou:
      # Checar os eventos do mouse aqui:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
        # atualiza desenho
        if cont == 60:

            funcoes()
            # for i in range(len(funcoes)):
            #     funcoes[i]()

            cont = 0
        # Atualiza o desenho na tela
        pygame.display.update()
        # 60 frames por segundo
        clock.tick(60)
        cont += 1