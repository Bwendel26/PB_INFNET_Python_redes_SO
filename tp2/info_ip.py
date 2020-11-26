import psutil

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
