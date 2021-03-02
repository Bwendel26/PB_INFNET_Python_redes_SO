import os
import os.path
import time


def dir_info(dir_path):
    os.chdir(dir_path)
    current_path = os.getcwd()
    status = os.stat(".\\")
    created_time = time.ctime(status.st_ctime)
    mod_time = time.ctime(status.st_mtime)

    path_list = current_path.split("\\")
    length_path_list = len(path_list) - 1
    name = path_list[length_path_list]

    final = "Current path:" + str(current_path) + \
            "\nPath name: " + name + \
            "\nCreated at: " + str(created_time) + \
            "\nLast modification date: " + str(mod_time)

    return final