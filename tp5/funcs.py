import psutil

def percentual_cpu():
    """
    This func uses the psutil lib to get and
    return the cpu used percent.
    :return: float percentual_usado
    """
    percentual_usado = psutil.cpu_percent(interval=0)
    return "CPU: " + str(percentual_usado) + "%"


def percentual_memoria():
    """
    This funcs use the psutil lib to get the memory
    used percent.
    :return: float percentual_usado
    """

    mem = psutil.virtual_memory().percent
    return "RAM: " + str(mem) + "%"


def info_battery():
    battery = psutil.sensors_battery()
    return "Bateria: " + str(battery.percent) + "%"


def informacao_ip():
    """
    This func return the IP computer`s address.
    :return ip:
    """

    dic_interface = psutil.net_if_addrs()
    ip = dic_interface["Ethernet"][1].address
    return "IP: " + str(ip)