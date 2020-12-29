import os
from typing import Optional
from typing import Sequence

from pluggy import PluginManager

from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl


class EphemeralCSVPlugin:
    def __init__(self, config: Configuration, plugin_manager: PluginManager) -> None:
        self.config = config
        self.plugin_manager = plugin_manager
        self.name = "CSV Plugin"

    @ephemeral_hookimpl
    def ephemeral_teardown(
        self, vulnerable_ports: Sequence[Optional[int]]
    ) -> Sequence[Optional[int]]:
        if vulnerable_ports:
            cwd = os.path.dirname(os.path.realpath(__file__))
            print(
                f"**** Writing vulnerable ports to disk, see: {os.path.join(cwd, 'vulnerable_ports.csv')}"
            )
            with open("vulnerable_ports.csv", "w") as f:
                f.write(", ".join([str(port) for port in vulnerable_ports]))
        return vulnerable_ports
