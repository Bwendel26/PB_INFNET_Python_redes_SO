import psutil
import platform

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

# print(informacao_cpu())