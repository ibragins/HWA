from psutil import virtual_memory
import multiprocessing
from LinuxHost import LinuxHost

mem = virtual_memory()
totalMemory = mem.total / 1024 / 1024
totalCores = multiprocessing.cpu_count()

myHost = LinuxHost(totalMemory, totalCores)

print(myHost)
