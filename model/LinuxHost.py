# import multiprocessing
# from psutil import virtual_memory

# mem = virtual_memory()
from model.DiskHost import DiskHost
from model.NetworkHost import NetworkHost


class LinuxHost:
    def __init__(self, json_obj):
        self.json_obj = json_obj
        self.total_ram = self.set_ram()
        self.total_cores = self.set_cores()  # = multiprocessing.cpu_count()
        self.volumes_list = self.set_volume()
        self.network_list = self.set_network()
        pass

    def __str__(self):
        volume_list_str = self.get_list_str()
        result = "\nCores:\t\t" + str(self.total_cores) + "\n"\
                 "Total RAM:\t" + self.total_ram + \
                 "\n" + volume_list_str + \
                 "\n"
        return result

    # def set_obj(self, j):
    #     spec = j['spec']
    #     domain = spec['domain']
    #     cpu = domain["cpu"]
    #     resources = domain["resources"]
    #     self.total_cores = cpu["cores"]
    #     self.total_ram = resources["requests"]["memory"]
    #     self.disks = domain['devices']['disks']

    def set_ram(self):
        return self.json_obj['spec']['domain']['resources']['requests']['memory']

    def set_cores(self):
        return self.json_obj['spec']['domain']['cpu']['cores']

    def set_network(self):
        network_list = []
        interfaces_json = self.json_obj['status']['interfaces']
        for cur_interface in interfaces_json:
            network = NetworkHost(cur_interface)
            network_list.append(network)
        return network_list

    def set_volume(self):
        volume_list = []
        volume_json = self.json_obj['spec']['volumes']
        for cur_volume in volume_json:
            volume = DiskHost(cur_volume)
            volume.diskName = cur_volume['name']
            volume.diskClaimName = cur_volume['persistentVolumeClaim']['claimName']
            volume_list.append(volume)
        return volume_list

    def get_list_str(self):
        result = "Disks:\n"
        for volume in self.volumes_list:
            result = result + volume.get_str()
        return result
