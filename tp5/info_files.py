import os
import os.path
import time


def file_info(file):
    path = ".\\"
    os.chdir(path)
    current_path = os.getcwd()
    status = os.stat(file)
    file_size = os.path.getsize(file)
    created_time = time.ctime(status.st_ctime)
    mod_time = time.ctime(status.st_mtime)
    name_type = str(file).split(".")

    final = "File name: " + name_type[0] + \
            "\nType: " + name_type[1] + \
            "\nLocation: " + str(current_path) + \
            "\nSize: " + str(file_size) + \
            "bytes.\nCreated at: " + created_time +\
            "\nLast modification: " + mod_time

    return final
