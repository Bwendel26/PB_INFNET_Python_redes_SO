import psutil
import pygame
import variaveis_interface as int_vars

#funcs
def informacao_ip():
    """
    Função que retorna o endereço de IP
    de um computador.
    :return ip:
    """

    dic_interface = psutil.net_if_addrs()
    ip = dic_interface["Ethernet"][1].address

    return ip

surface5 = int_vars.s5

def mostra_info_ip():
    int_vars.tela.fill(int_vars.BRANCO)
    info = informacao_ip()
    texto_barra = "Info: " + str(info)
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface5, (0, 3*int_vars.tela_altura / 4))  # setando divisao tela
    int_vars.tela.blit(text, (20, 4*int_vars.tela_altura / 4))


print(informacao_ip())