import os
import os.path


def dir_info():
    return os.getcwd()


print(dir_info())
print(os.path.getsize("./info_dir.py"), "bytes")
