import socket
import typing
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue

from halo import Halo

from zonic.abc.base_classes import Scanable
from zonic.configuration import Configuration
from zonic.results import ScanResult


class Scanner(Scanable):
    def __init__(self, config: Configuration):
        self.config = config
        self.infinite_queue: Queue[ScanResult] = Queue()
        self.executor = ThreadPoolExecutor(
            max_workers=self.config.thread_count, thread_name_prefix="Scanner"
        )

    def scan(self, port: int) -> ScanResult:
        socket_data = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        try:
            return ScanResult(
                port, not bool(socket_data.connect_ex((self.config.target, port)))
            )
        except socket.error:
            return ScanResult(port, False)

    def scan_ports(self, ports: typing.Iterable[int]) -> typing.List[ScanResult]:
        futures = []
        with Halo(text="***** Port scanning in progress...", color="blue"):
            with self.executor as executor:
                for port in ports:
                    futures.append(executor.submit(self.scan, port))

            return [x for x in [f.result() for f in as_completed(futures)] if x.is_open]
