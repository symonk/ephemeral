import os
from typing import Optional
from typing import Sequence

from pluggy import PluginManager

from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl


class CSVPlugin:
    def __init__(self, config: Configuration, plugin_manager: PluginManager) -> None:
        self.config = config
        self.plugin_manager = plugin_manager

    @ephemeral_hookimpl
    def ephemeral_teardown(
        self, vulnerable_ports: Sequence[Optional[int]]
    ) -> Sequence[Optional[int]]:
        if vulnerable_ports:
            print(
                f"**** Writing vulnerable ports to disk, see: {os.path.join(os.path.curdir, 'vulnerable_ports.csv')}"
            )
            with open("vulnerable_ports.csv", "w+"):
                ",".join([str(port) for port in vulnerable_ports])
        return vulnerable_ports
