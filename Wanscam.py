import requests

from helpers.devices.CameraDevice import CameraDevice


class Wanscam(CameraDevice):
    def __init__(self, ip, port=99, user='admin', password=''):
        super(Wanscam, self).__init__()
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

    def make_snapshot(self):
        """Use camera to make a snapshot"""
        result = self.__send('snapshot.cgi')
        return result.content if result.status_code == 200 else None

    def move_bottom(self):
        """Move camera to down"""
        self.__send_command(2)

    def move_left(self):
        """Move camera to left"""
        self.__send_command(6)

    def move_right(self):
        """Move camera to right"""
        self.__send_command(4)

    def move_top(self):
        """Move camera to up"""
        self.__send_command(0)

    def __send(self, page):
        return requests.get('http://%s:%d/%s' % (self.ip, self.port, page), auth=(self.user, self.password))

    def __send_command(self, commande_id):
        return self.__send('decoder_control.cgi?command=%s' % commande_id)