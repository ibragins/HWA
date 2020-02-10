class DiskHost:
    def __init__(self, json_obj):
        self.json_obj = json_obj
        self.diskName = None
        # self.diskSize = None
        self.diskClaimName = None

    def __str__(self):
        return "Disk name:\t\t" + self.diskName + \
               "\nDisk Claim Name:\t" + self.diskClaimName + \
               "\n"

    def get_str(self):
        return "\tDisk name:\t\t\t" + self.diskName + \
               "\n\tDisk Claim Name:\t" + self.diskClaimName + \
               "\n\t---\n"
