import psutil
import platform
import variaveis_interface as int_vars
import pygame

#funcs
def informacao_cpu():
    """
    Função que retorna as informações da CPU de
    um computador.
    :return informação:
    """
    num_cores = psutil.cpu_count()
    num_cores_reais = psutil.cpu_count(logical=False) #numero de processadores s/ contar os lógicos (hyper-thread CPU cores).
    processador_bits = platform.processor()
    processador_nome = platform.node()
    processador_detalhes = platform.platform()
    sistema_operacional = platform.system()

    informacao = "Processador:\nNome computador: {}\nN° de cores: {}.\nN° de cores reais: {}." \
                 "\nArquitetura de {}\nSistema Operacional: {}\nDetalhes: {}" \
                 "".format(processador_nome, num_cores, num_cores_reais, processador_bits, sistema_operacional, processador_detalhes)

    return informacao

surface4 = int_vars.s4

def mostra_info_cpu():
    int_vars.tela.fill(int_vars.PRETO)
    info = informacao_cpu()
    texto_barra = "Info:" + str(info)
    text = int_vars.font.render(texto_barra, 1, int_vars.BRANCO)
    int_vars.tela.blit(surface4, (0, 3*int_vars.tela_altura / 4))  # setando divisao tela
    int_vars.tela.blit(text, (20, 3*int_vars.tela_altura / 4))