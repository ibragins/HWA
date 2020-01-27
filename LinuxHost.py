import multiprocessing
from psutil import virtual_memory
mem = virtual_memory()


class LinuxHost:
    def __init__(self):
        self.total_ram = mem.total / 1024 / 1024
        self.total_cores = multiprocessing.cpu_count()

    def __str__(self):
        return "Total RAM:\t" + str(self.total_ram) + "\nCores:\t\t" + str(self.total_cores) + "\n"
