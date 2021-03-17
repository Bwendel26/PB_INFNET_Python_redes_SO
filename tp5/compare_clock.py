"""
Dentro do escalonamento realizado na questão anterior, realizar
uma comparação dos tempos obtidos com a quantidade total de
clocks utilizados pela CPU para a realização dessas mesmas chamadas.

 - Indique a diferença de tempo real e tempo do clock do computador.
 - Indique o que acontece com essa diferença quando insere um tempo
    de espera, como por exemplo utilizando o ‘time.sleep’ dentro de alguma chamada.
"""

import psutil
import time
import sched

scheduler = sched.scheduler(time.time, time.sleep)

print("Frequência max da CPU: " + str(psutil.cpu_freq().max) + "GHz.")


def print_scheduled(func, name=None):
    try:
        print("\nInfo: ", func(), " ")
    except:
        print("\nInfo: ", func())


def cpu_current_freq():
    return psutil.cpu_freq().current


def main():
    start = time.time()
    print('INICIO:', time.ctime())
    scheduler.enter(2, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(3, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(4, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(5, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(6, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(7, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(8, 1, print_scheduled, (cpu_current_freq,))
    scheduler.enter(9, 1, print_scheduled, (cpu_current_freq,))
    print('CHAMADAS ESCALONADAS:')

    scheduler.run()

    finish = time.time()

    print("\nFIM: " + time.ctime())

    total_secs = abs(finish - start)
    print(f"Tempo total: {total_secs:.0f} segundos")


main()