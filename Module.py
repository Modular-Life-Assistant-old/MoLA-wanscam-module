from helpers.modules.DevicesModule import DevicesModule
from .Wanscam import Wanscam


class Module(DevicesModule):
    wait_next_update = 1
    device_class = Wanscam

    def device_on_network(self, ip, mac):
        """Device are detected on network

        :param ip: ip adress
        :param mac: mac adress
        """
        # is compatible device ?
        if not mac.startswith('0018fb'):
            return

        # is already added
        for device in self.devices.values():
            if ip == device.ip:
                return

        self.add_device(ip)