import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from queue import Queue
from typing import Iterable
from typing import List
from typing import Optional

from halo import Halo

from ephemeral.decorators import stdout_scan_time


class PortScanner:
    def __init__(
        self,
        target: str,
        port_range: Iterable[int],
        quick: bool,
        random: bool,
        thread_count: int,
    ) -> None:
        self.target = socket.gethostbyname(target)
        self.port_range = port_range
        self.quick = quick
        self.random = random
        self.thread_count = thread_count
        self.ports_queue: Queue = Queue(maxsize=socket.SOL_SOCKET + 1)

    @stdout_scan_time
    def attack(self) -> List[Optional[int]]:
        executor = ThreadPoolExecutor(max_workers=self.thread_count)
        futures = []
        with Halo(text="***** Port scanning in progress...", color="blue"):
            for port in self.port_range:
                futures.append(executor.submit(self.scan_port, port))
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    self.ports_queue.put(result)
            return list(self.ports_queue.queue)

    def scan_port(self, port: int) -> Optional[int]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((self.target, port))
            if result == 0:
                return port
        return None
