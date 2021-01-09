import argparse
from datetime import datetime
from typing import Optional
from typing import Sequence

from colorama import Fore
from pluggy import PluginManager

from sonic import Configuration
from sonic import sonic_hookimpl
from sonic.scanner import PortScanner


class SonicCorePlugin:
    def __init__(self, config: Configuration, plugin_manager: PluginManager) -> None:
        self.config = config
        self.plugin_manager = plugin_manager
        self.name = "Sonics Base Plugin"
        self.scanner = PortScanner(
            config.target,
            config.port_range,
            config.quick,
            config.random,
            config.thread_count,
        )

    @sonic_hookimpl
    def sonic_setup(self) -> None:
        print(f"**** Sonic started at: {self._get_datetime_now()}")
        ignored = ("plugin_manager",)
        for setting, value in {
            k: v for k, v in vars(self.config).items() if k not in ignored
        }.items():
            print(
                f"**** [{Fore.BLUE + setting + Fore.RESET} = {Fore.GREEN + str(value) + Fore.RESET}] *****"
            )

    @sonic_hookimpl
    def sonic_execute(self) -> Sequence[Optional[int]]:
        return self.scanner.attack(self.config.get_option("random"))

    @sonic_hookimpl
    def sonic_teardown(
        self, vulnerable_ports: Sequence[Optional[int]]
    ) -> Sequence[Optional[int]]:
        return []

    @sonic_hookimpl
    def sonic_report(self, ports: Sequence[Optional[int]]) -> None:
        print(
            f"**** {Fore.RED}Vulnerable {Fore.RESET}ports => {Fore.YELLOW} {list(ports)} {Fore.RESET}"
        )

    @staticmethod
    def _get_datetime_now() -> str:
        return datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")

    @staticmethod
    def print_in_color(color: Fore, message: str) -> None:
        print(f"{color} {message} {Fore.RESET}")