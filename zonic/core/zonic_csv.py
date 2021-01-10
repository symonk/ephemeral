import argparse
from typing import Optional
from typing import Sequence

from pluggy import PluginManager

from zonic import Configuration
from zonic import zonic_hookimpl


class ZonicCSVPlugin:
    def __init__(self, plugin_manager: PluginManager) -> None:
        self.plugin_manager = plugin_manager
        self.name = "CSV Plugin"

    @zonic_hookimpl
    def zonic_add_options(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "-wv",
            "--write-vulnerable",
            action="store_true",
            default=False,
            help="If vulnerable ports are detected; write them to csv in the cwd",
            dest="write_vulnerable",
        )

    @zonic_hookimpl
    def zonic_teardown(
        self, config: Configuration, vulnerable_ports: Sequence[Optional[int]]
    ) -> Sequence[Optional[int]]:
        if vulnerable_ports and config.get_option("write_vulnerable"):
            print("**** Writing vulnerable ports to disk, see: `vulnerable_ports.csv`")
            with open("vulnerable_ports.csv", "w") as f:
                f.write(f"[Target]: {config.target}\n")
                f.write(", ".join([str(port) for port in vulnerable_ports]))
        return vulnerable_ports
