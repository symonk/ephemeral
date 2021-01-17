import socket
import typing

from zonic.abc.base_classes import Scanable
from zonic.configuration import Configuration


class Scanner(Scanable):
    def __init__(self, config: Configuration):
        self.config = config

    def scan(self, port: int) -> typing.Tuple[int, bool, int]:
        socket_data = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        try:
            result = socket_data.connect_ex((self.config.target, port))
            return port, True, result
        # TODO: Less broad here
        except Exception:
            return port, False, -1
