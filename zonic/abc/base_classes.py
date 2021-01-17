import abc
import typing

from zonic.results import ScanResult
from zonic.utility.string_utils import StringTemplate


class Attackable(abc.ABC):
    @abc.abstractmethod
    def attack(self, port_range: typing.Iterable[int]) -> typing.List[ScanResult]:
        """
        Begin attacking ports in the port range
        """
        ...


class Scanable(abc.ABC):
    @abc.abstractmethod
    def scan(self, port: int) -> ScanResult:
        """
        Perform a port scan against a particular port.
        :param port: The port (integer) to perform the scan against
        :return: A tuple of (port_number, boolean, ACK sequence) to indicate if port was considered `open`
        """
        ...

    @abc.abstractmethod
    def scan_ports(self, ports: typing.Iterable[int]) -> typing.List[ScanResult]:
        """
        Perform a larger scan of a selections of ports
        :param ports: An iterable of ports (int)
        :return: A List of ScanResults which encapsulate connect_ex data
        """
        ...


class Writable(abc.ABC):
    @abc.abstractmethod
    def write(self, template: StringTemplate, flush: bool = True) -> None:
        """
        Write messages to standard out
        :param template: StringTemplate instance to be written to stdout
        :param flush: A boolean flag to indicate if a flush should be performed after
        """
        ...
