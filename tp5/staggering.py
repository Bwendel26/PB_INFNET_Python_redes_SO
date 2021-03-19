"""
Realizar um escalonamento das chamadas das funções com o módulo ‘sched’
e medir o tempo total utilizado por cada chamada com o módulo ‘time’.
Você pode escolher com quais funções do seu projeto realizar o
escalonamento, deixando indicado no relatório.
"""
import time
import sched
import funcs
scheduler = sched.scheduler(time.time, time.sleep)


def print_scheduled(func, name=None):
    try:
        print("\nInfo: ", func(name), " ")
    except:
        print("\nInfo: ", func())


def main():
    start = time.time()
    print('INICIO:', time.ctime())
    scheduler.enter(2, 1, print_scheduled, (funcs.percentual_cpu,))
    scheduler.enter(3, 1, print_scheduled, (funcs.percentual_memoria,))
    scheduler.enter(4, 1, print_scheduled, (funcs.informacao_ip,))
    scheduler.enter(5, 1, print_scheduled, (funcs.info_battery,))
    print('CHAMADAS ESCALONADAS:')

    scheduler.run()

    finish = time.time()

    print("\nFIM: " + time.ctime())

    total_secs = abs(finish - start)
    print(f"Tempo total: {total_secs:.0f} segundos")


main()