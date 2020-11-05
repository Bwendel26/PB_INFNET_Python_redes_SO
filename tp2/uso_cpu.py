import psutil

#funcs
def percentual_cpu(tempo):
    """
    Função que retorna o percentual de uso da CPU
    do computador.
    :param tempo: em segundos para retornar o percentual.
    :return: float percentual_usado
    """
    percentual_usado = psutil.cpu_percent(tempo)

    return percentual_usado

# while True:
#     print(percentual_cpu(1))