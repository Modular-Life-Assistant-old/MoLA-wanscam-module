import requests

from helpers.devices.CameraDevice import CameraDevice


DEFAULT_PASSWORD = ''
DEFAULT_PORT = 99
DEFAULT_USER = 'admin'


class Wanscam(CameraDevice):
    def __init__(self, ip, name='Wanscam', port=DEFAULT_PORT, user=DEFAULT_USER,
                 password=DEFAULT_PASSWORD):
        super(Wanscam, self).__init__()
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

        if name:
            self.name = name

    def get_config(self):
        """Get config info to save (passed on constructor on restart)

        :return: list of object parameters
        """
        kwargs_index = ('name', 'port', 'user', 'password')
        kwargs = {i: getattr(self, i) for i in kwargs_index}
        return {'args': [self.ip], 'kwargs': kwargs}

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

    def move_stop(self):
        """Stop camera mouving"""
        self.__send_command(1)

    def move_top(self):
        """Move camera to up"""
        self.__send_command(0)

    def __send(self, page):
        try:
            return requests.get('http://%s:%d/%s' % (self.ip, self.port, page), auth=(self.user, self.password))
        except Exception as e:
            self.add_error('Device unusable: %s' % e)
            result = requests.Response()
            result.status_code = 503  # Service Unavailable
            return result

    def __send_command(self, command_id):
        return self.__send('decoder_control.cgi?command=%s' % command_id)
