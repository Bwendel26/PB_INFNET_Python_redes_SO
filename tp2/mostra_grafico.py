import pygame
import psutil

pygame.font.init()
font = pygame.font.Font(None, 32)

azul = (0, 0, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)


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

tela = tela_pygame()
largura_tela = tela_pygame()[0]

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2 * 20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))

cont = 60

terminou = False

while not terminou:
  # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    # Fazer a atualização a cada segundo:
    if cont == 60:
      mostra_uso_memoria()
      cont = 0
    # Atualiza o desenho na tela
    pygame.display.update()
    # 60 frames por segundo
    pygame.clock.tick(60)
    cont = cont + 1