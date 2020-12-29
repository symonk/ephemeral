from datetime import datetime
from typing import Optional
from typing import Sequence

from colorama import Fore
from pluggy import PluginManager

from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl
from ephemeral.scanner import PortScanner


class EphemeralCorePlugin:
    def __init__(self, config: Configuration, plugin_manager: PluginManager) -> None:
        self.config = config
        self.plugin_manager = plugin_manager
        self.name = "Ephemeral Base Plugin"
        self.scanner = PortScanner(
            config.target,
            config.port_range,
            config.quick,
            config.random,
            config.thread_count,
        )

    @ephemeral_hookimpl
    def ephemeral_setup(self) -> None:
        print(f"**** Ephemeral setup started at: {self._get_datetime_now()}")
        ignored = ("plugin_manager",)
        for setting, value in {
            k: v for k, v in vars(self.config).items() if k not in ignored
        }.items():
            print(
                f"**** [{Fore.BLUE + setting + Fore.RESET} = {Fore.GREEN + str(value) + Fore.RESET}] *****"
            )

    @ephemeral_hookimpl
    def ephemeral_execute(self) -> Sequence[Optional[int]]:
        return self.scanner.attack(self.config.random)

    @ephemeral_hookimpl
    def ephemeral_teardown(self) -> Sequence[Optional[int]]:
        return []

    @ephemeral_hookimpl
    def ephemeral_report(self, ports: Sequence[Optional[int]]) -> None:
        for port in ports:
            print(
                f" **** Port: {Fore.GREEN + str(port) + Fore.RESET} is potentially {Fore.RED} vulnerable! {Fore.RESET}"
            )

    @staticmethod
    def _get_datetime_now() -> str:
        return datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")

    @staticmethod
    def print_in_color(color: Fore, message: str) -> None:
        print(f"{color} {message} {Fore.RESET}")
