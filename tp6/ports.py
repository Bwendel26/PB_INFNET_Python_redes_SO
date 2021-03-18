"""
Criar uma ou mais funções que retornem ou apresentem
informações sobre as portas dos diferentes IPs obtidos nessa sub rede.
"""
import os
import subprocess
import platform
import nmap

nmScan = nmap.PortScanner()


def scan_host(host):

    nmScan.scan(host)
    print(nmScan[host].hostname())
    for proto in nmScan[host].all_protocols():
        print('----------')
        print('Protocolo : %s' % proto)

        lport = nmScan[host][proto].keys()
        #lport.sort()
        for port in lport:
            print ('Porta: %s\t Estado: %s' % (port, nmScan[host][proto][port]['state']))


def ping_code(hostname):
    """
    Uses the ping of the OS.
    ('-c 5'): Says that linux that have to send 5 packates.
    ('-W 3'): Says that the linux have to wait 3
    miliseconds for an answer. that func return the ping response
    """

    plataforma = platform.system()
    args = []
    if plataforma == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    ret_cod = subprocess.call(args, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
    return ret_cod


def verify_hosts(base_ip):
    """
    verify all hosts with the base ip between 1 and 255 returns a
    list with all hosts that had 0 responses(active).
    """
    print("Mapeando\r")
    host_validos = []
    return_codes = dict()
    for i in range(1, 255):

        return_codes[base_ip + '{0}'.format(i)] = ping_code(base_ip + '{0}'.format(i))
        if i % 20 == 0:
            print(".", end="")
        if return_codes[base_ip + '{0}'.format(i)] == 0:
            host_validos.append(base_ip + '{0}'.format(i))
    print("\nMapping ready...")

    return host_validos


def main():
    for item in host_validos:
        print("Verificando", item)
        print(scan_host(item))
        print("\n")



# MAIN
ip_string = input("Entre com o ip alvo: ")
ip_lista = ip_string.split(".")
base_ip = ".".join(ip_lista[0:3]) + "."
print("O teste será feito na sub-rede: ", base_ip, "\n")
host_validos = verify_hosts(base_ip)
main()