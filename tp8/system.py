import os
import cpuinfo
import psutil
import subprocess
import time
from psutil._common import bytes2human

class System_Info():
    ''' This class retrieves some types of system information. '''
    def __init__(self):
        ''' Constructor. '''
        self.cpu_info = cpuinfo.get_cpu_info()
        self.cpu_count_phisycal = psutil.cpu_count(logical=False)
        self.cpu_count_logical = psutil.cpu_count(logical=True)
        self.cpu_percent = psutil.cpu_percent(interval=None, percpu=True)
        self.disk_usage = psutil.disk_usage('/')
        self.network = psutil.net_if_addrs()

    def memory(self):
        ''' This function returns a dict of memory informations. '''
        def format_info(info):
            dict_info = dict()
            for name in info._fields:
                value = getattr(info, name)
                if name != 'percent':
                    value = bytes2human(value)
                dict_info[name.capitalize()] = value
            return dict_info

        memory = format_info(psutil.virtual_memory())
        swap = format_info(psutil.swap_memory())
        return memory, swap

    def _disk_usage(self):
        ''' This function returns a dict of disk partitions and your usages. '''
        usage_dict = dict()
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            usage_dict[part.device] = [bytes2human(usage.total),
                                       bytes2human(usage.used),
                                       bytes2human(usage.free),
                                       int(usage.percent),
                                       part.fstype,
                                       part.mountpoint]
        return usage_dict

    def _cpu_info(self):
        ''' This function returns a dictionary with informations about the cpu. '''
        cpu_dict = dict()
        cpu_dict['Name: '] = self.cpu_info['brand_raw']
        cpu_dict['Architecture: '] = self.cpu_info['arch']
        cpu_dict['Bits: '] = self.cpu_info['bits']
        if self.cpu_info['hz_actual'][0] % 10**9 > 0:
            cpu_dict['Frequency: '] = str(
                round((self.cpu_info['hz_actual'][0]/10**9), 2)) + ' Ghz'
        elif self.cpu_info['hz_actual'][0] % 10**6 > 0:
            cpu_dict['Frequency: '] = str(
                round((self.cpu_info['hz_actual'][0]/10**9), 2)) + ' Mhz'
        elif self.cpu_info['hz_actual'][0] % 10**3 > 0:
            cpu_dict['Frequency: '] = str(
                round((self.cpu_info['hz_actual'][0]/10**9), 2)) + ' Khz'
        cpu_dict['Physical Cores: '] = self.cpu_count_phisycal
        cpu_dict['Logical Cores: '] = self.cpu_count_logical
        cpu_dict['cpus'] = self.cpu_percent
        return cpu_dict

    def _network(self):
        ''' This function get the addresses associated to each network
        interface card (NIC) installed on the system and put in a dict
        {NIC: IP}. '''
        network = {}
        for k, v in self.network.items():
            if k == 'Loopback Pseudo-Interface 1':
                network[k] = [v[0].address]
            else:
                network[k] = [v[1].address]
        return network

    def _info_files(self):
        lista = os.listdir()
        dic = dict()
        for i in lista:
            dic[i] = []
            if os.path.isfile(i):
                dic[i].append(bytes2human(os.stat(i).st_size))
                dic[i].append(time.ctime(os.stat(i).st_atime))
                dic[i].append(time.ctime(os.stat(i).st_mtime))
                dic[i].append(os.path.splitext(i)[1])
                dic[i].append('File')
            else:
                dic[i].append(bytes2human(os.stat(i).st_size))
                dic[i].append(time.ctime(os.stat(i).st_atime))
                dic[i].append(time.ctime(os.stat(i).st_mtime))
                dic[i].append(os.path.splitext(i)[1])
                dic[i].append('Directory')
        return dic

    def _directory_info(self):
        lista = os.listdir()
        dic = dict()
        for i in lista:
            dic[i] = []
            if os.path.isfile(i):
                dic[i].append(bytes2human(os.stat(i).st_size))
                dic[i].append(time.ctime(os.stat(i).st_atime))
                dic[i].append(time.ctime(os.stat(i).st_mtime))
                dic[i].append(os.path.splitext(i)[1])
                dic[i].append('File')
            else:
                dic[i].append(bytes2human(os.stat(i).st_size))
                dic[i].append(time.ctime(os.stat(i).st_atime))
                dic[i].append(time.ctime(os.stat(i).st_mtime))
                dic[i].append(os.path.splitext(i)[1])
                dic[i].append('Directory')
        return dic

    def _pid_info(self):
        name = 'python.exe'
        lp = psutil.pids()
        pid_list = []
        for i in lp:
            p = psutil.Process(i)
            if p.name() == name:
                pid_list.append(i)
        return pid_list