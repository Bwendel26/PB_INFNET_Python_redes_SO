import psutil

#variaveis
memoria = psutil.virtual_memory()

#funcs
def percentual_memoria():
    """
    Função que retorna o percentual de memoria RAM
    utilizado por um computador.
    :return: float percentual_usado
    """
    total_gb = round((memoria.total/(1024 ** 3)), 3)
    usada_gb = round((memoria.used/(1024 ** 3)), 3)
    percentual_usado = (usada_gb * 100) / total_gb

    return round(percentual_usado, 3)

# print(percentual_memoria())