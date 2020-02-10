class NetworkHost:
    def __init__(self, json_obj):
        self.json_obj = json_obj
        self.interfaceName = self.set_interface_name()
        self.ipAddress = self.set_ip_address()
        self.mac = json_obj['mac']

    def set_interface_name(self):
        try:
            return self.json_obj['interfaceName']
        except:
            return None

    def set_ip_address(self):
        try:
            return self.json_obj['ipAddress']
        except:
            return None

    def __str__(self):
        return
