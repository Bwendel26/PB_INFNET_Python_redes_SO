"""
Criar uma ou mais funções que retornem ou apresentem
informações sobre diretórios e arquivos. Tais informações
podem ser qualquer uma que você achar relevante disponível
no módulo ‘os’ e ‘psutil’ de Python, como nome, tamanho,
localização, data de criação, data de modificação, tipo, etc.
"""
import os
import os.path
import time


def dir_info(dir_path):
    os.chdir(dir_path)
    current_path = os.getcwd()
    status = os.stat(".\\")
    created_time = time.ctime(status.st_ctime)
    mod_time = time.ctime(status.st_mtime)

    final = "Current path:" + str(current_path) + \
            "\nPath name: " + "Name" + \
            "\nCreated at: " + created_time + \
            "\nLast modification date: " + mod_time

    return final