import pygame

def loop_relogio(funcoes):
    # cria relogio
    clock = pygame.time.Clock()
    cont = 60

    terminou = False
    func_atual = 0 #controle de funcao aprensentada

    while not terminou:
      # Checar os eventos do mouse aqui:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    func_atual += 1
                    if func_atual >= len(funcoes):
                        func_atual = 0
                    funcoes[func_atual]()
                if event.key == pygame.K_LEFT:
                    func_atual -= 1
                    if func_atual < 0:
                        func_atual = len(funcoes) - 1
                    funcoes[func_atual]()

        # atualiza desenho
        if cont == 60:
            funcoes[func_atual]()
            # for i in range(len(funcoes)):
            #     funcoes[i]()

            cont = 0
        # Atualiza o desenho na tela
        pygame.display.update()
        # 60 frames por segundo
        clock.tick(60)
        cont += 1