"""
Criar uma ou mais funções que retornem ou apresentem
informações sobre processos do sistema. As informações
podem ser: PID, nome do executável, consumo de processamento,
consumo de memória, entre outras disponíveis no módulo ‘psutil’ de Python.
"""
import psutil
import datetime
import pygame
import variaveis_interface as iv
from clock import clock_pygame as clock


def process_info(p_name):
    pid = False
    name = p_name
    c_time = 0
    p_mem = 0

    for procs in psutil.process_iter(["pid", "name", "username"]):
        if str(procs.name()) == name:
            c_time = datetime.datetime.fromtimestamp(procs.create_time()).strftime("%Y-%m-%d %H:%M:%S")
            pid = str(procs.pid)
            p_mem = procs.memory_info()
    if pid:
        return "Process name: " + name + \
               "\nPid: " + pid + \
               "\nCreation time: " + c_time + \
               "\nMemory consumed: " + str(p_mem.rss)

    else:
        return "This process do not exist."



e_info = str(input("Insert the name of the process (Ex: firefox.exe): "))

# View: Pygame
pygame.display.set_caption("System process")
surface = pygame.surface.Surface((iv.tela_largura, iv.tela_altura))
tela = pygame.display.set_mode((iv.tela_largura, iv.tela_altura))
pygame.init()
pygame.display.init()
pygame.font.init()
font = pygame.font.Font(None, 32)
iv.tela.fill(iv.PRETO)`
info = process_info(e_info)
text_info = "Info: " + str(info)
text = iv.font.render(text_info, 1, iv.BRANCO)
iv.tela.blit(surface, (0, 1 * iv.tela_altura))  # setando divisao tela
iv.tela.blit(text, (20, 1 * iv.tela_altura))

clock()