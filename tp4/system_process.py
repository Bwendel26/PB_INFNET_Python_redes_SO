"""
Criar uma ou mais funções que retornem ou apresentem
informações sobre processos do sistema. As informações
podem ser: PID, nome do executável, consumo de processamento,
consumo de memória, entre outras disponíveis no módulo ‘psutil’ de Python.
"""
import psutil
import datetime


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


print(process_info("firefox.exe"))