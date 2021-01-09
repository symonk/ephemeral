from typing import Optional
from typing import Sequence

from pluggy import PluginManager

from zonic import Configuration
from zonic import zonic_hookimpl


class ZonicCSVPlugin:
    def __init__(self, config: Configuration, plugin_manager: PluginManager) -> None:
        self.config = config
        self.plugin_manager = plugin_manager
        self.name = "CSV Plugin"

    @zonic_hookimpl
    def zonic_teardown(
        self, vulnerable_ports: Sequence[Optional[int]]
    ) -> Sequence[Optional[int]]:
        if vulnerable_ports and self.config.write_vulnerable:
            print("**** Writing vulnerable ports to disk, see: `vulnerable_ports.csv`")
            with open("vulnerable_ports.csv", "w") as f:
                f.write(f"[Target]: {self.config.target}\n")
                f.write(", ".join([str(port) for port in vulnerable_ports]))
        return vulnerable_ports
