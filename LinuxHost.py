class LinuxHost:
    def __init__(self, ram, cores):
        self.total_ram = ram
        self.total_cores = cores

    def __str__(self):
        return "Total RAM:\t" + str(self.total_ram) + "\nCores:\t\t" + str(self.total_cores) + "\n"
