"""
Utilizar o módulo ‘sched’ para chamar as funções criadas
no TP4 que retornam as informações sobre diretórios e arquivos.
"""
from info_dir import dir_info
from info_files import file_info
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

dir = str(input("Entre com o caminho do diretório (Ex: ./../): "))
file = str(input("Entre com o nome do arquivo (Ex: call_funcs.py): "))


def print_scheduled(func, name):
    print("\nInformações sobre o arquivo/diretório escolhidos:\n", func(name))


print('INICIO:', time.ctime())
scheduler.enter(2, 1, print_scheduled, (dir_info, dir,))
scheduler.enter(3, 1, print_scheduled, (file_info, file,))
print('CHAMADAS ESCALONADAS:')

scheduler.run()