from helpers.modules.DevicesModule import DevicesModule
from .Wanscam import Wanscam


class Module(DevicesModule):
    wait_next_update = 1

    def init(self):
        self.add_device(Wanscam('192.168.1.2', 80, 'mola', 'KGwErtlWkJ08'))

    def search_new(self):
        """Search new devices

        :return: list of device object
        """
        return []