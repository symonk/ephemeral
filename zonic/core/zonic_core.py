import argparse
from datetime import datetime
from typing import List
from typing import Optional
from typing import Sequence

from colorama import Fore
from pluggy import PluginManager

from zonic import Configuration
from zonic import zonic_hookimpl
from zonic.scanner import PortScanner


class ZonicCorePlugin:
    def __init__(self, plugin_manager: PluginManager) -> None:
        self.plugin_manager = plugin_manager
        self.name = "Zonics Base Plugin"

    @zonic_hookimpl
    def zonic_add_options(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--target",
            action="store",
            help="The target host to inspect available ports of.",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            help="Run zonic in verbose mode",
            dest="verbose",
        )
        parser.add_argument(
            "-q",
            "--quick",
            action="store_true",
            help="Scan only the top 100 popular open ports",
            dest="quick",
        )
        parser.add_argument(
            "-r",
            "--random",
            action="store_true",
            help="Scan ports in the port range randomly, not sequentially.",
            dest="random",
        )
        parser.add_argument(
            "-tc",
            "--thread-count",
            action="store",
            type=int,
            default=5_000,
            help="How many threads should scanning use, this depends heavily on available memory, tweak accordingly.",
            dest="thread_count",
        )
        parser.add_argument(
            "-pr",
            "--ports",
            action="store",
            type=int,
            default=range(65536),
            help="Specify the port range to perform a scan on.",
            dest="port_range",
        )

    @zonic_hookimpl
    def zonic_setup(self, config: Configuration) -> None:
        print(f"**** zonic started at: {self._get_datetime_now()}")
        ignored = ("plugin_manager",)
        for setting, value in {
            k: v for k, v in vars(config).items() if k not in ignored
        }.items():
            print(
                f"**** [{Fore.BLUE + setting + Fore.RESET} = {Fore.GREEN + str(value) + Fore.RESET}] *****"
            )

    @zonic_hookimpl
    def zonic_execute(self, config: Configuration) -> List[Optional[int]]:
        scanner = PortScanner(
            config.target,
            config.port_range,
            config.quick,
            config.random,
            config.thread_count,
        )
        return [int(x) for x in scanner.attack(config.get_option("random"))]

    @zonic_hookimpl
    def zonic_teardown(
        self, vulnerable_ports: Sequence[Optional[int]]
    ) -> Sequence[Optional[int]]:
        return []

    @zonic_hookimpl
    def zonic_report(self, ports: Sequence[Optional[int]]) -> None:
        print(
            f"**** {Fore.RED}Vulnerable {Fore.RESET}ports => {Fore.YELLOW} {list(ports)} {Fore.RESET}"
        )

    @staticmethod
    def _get_datetime_now() -> str:
        return datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")

    @staticmethod
    def print_in_color(color: Fore, message: str) -> None:
        print(f"{color} {message} {Fore.RESET}")
