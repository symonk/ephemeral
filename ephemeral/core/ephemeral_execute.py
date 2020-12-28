from typing import Optional
from typing import Sequence

from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl
from ephemeral.scanner import PortScanner


@ephemeral_hookimpl
def ephemeral_execute(config: Configuration) -> Sequence[Optional[int]]:
    config.terminal_writer.announce_execute()
    scanner = PortScanner(
        config.target,
        config.port_range,
        config.quick,
        config.random,
        config.thread_count,
    )
    ports = scanner.attack()
    return ports
