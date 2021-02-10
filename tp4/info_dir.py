"""
Criar uma ou mais funções que retornem ou apresentem
informações sobre diretórios e arquivos. Tais informações
podem ser qualquer uma que você achar relevante disponível
no módulo ‘os’ e ‘psutil’ de Python, como nome, tamanho,
localização, data de criação, data de modificação, tipo, etc.
"""
import os
import os.path
import psutil


def dir_info(dir_path, file_path):

    path = dir_path
    os.chdir(path)
    current_path = os.getcwd()
    file_size = os.path.getsize(file_path)

    final = "current path:", str(current_path), "\nfile name:", \
            "Name  -- size:", file_size,  "bytes."

    return final

print(dir_info("./", "info_dir.py"))