"""
Crie uma ou mais funções que retornem ou apresentem as seguintes 
informações de redes: IP, gateway, máscara de subrede.
"""
# import psutil
import socket
import os


def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def default_gateway():
    if os.name == "posix":
        dgw = os.system('ip r | grep default | awk {"print $3"}')
        return dgw
    if os.name == "nt":
        dgw = os.system('ipconfig | findstr /i "Gateway"')
        return dgw


def subnet_mask():
    if os.name == "posix":
        sm = os.system('ip r | grep default | awk {"print $3"}')
        return sm
    if os.name == "nt":
        sm = os.system('ipconfig | findstr /i "Subnet"')
        return sm


#MAIN
#ARRUMAR FORMATACAO
def main():
    print("Dados da rede: ")
    default_gateways = default_gateway()
    subnet_masks = subnet_mask()
    print("\nIP:", ip())
    print("\n" + "-" * 35)

main()

# interfaces = psutil.net_if_addrs()
# names = []
# # get the interfaces names
# for i in interfaces:
#     names.append(str(i))
# # print the values
# for i in names:
#     print(i + ":")
#     for j in interfaces[i]:
#         print("\t" + str(j))


