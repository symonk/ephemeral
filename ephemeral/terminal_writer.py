from datetime import datetime
from typing import Mapping

from colorama import Fore


class TerminalWriter:
    def __init__(self, options: Mapping[str, str]) -> None:
        self.options = options

    def announce_setup(self) -> None:
        self.print_in_color(
            Fore.GREEN, f"[Ephemeral setup started at: {self._get_datetime_now()}]"
        )
        for setting, value in self.options.items():
            print(f"**** [{setting} = {value}] *****")

    @staticmethod
    def _get_datetime_now() -> str:
        return datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")

    def announce_execution(self) -> None:
        self.print_in_color(Fore.GREEN, "[Ephemeral execution has begun...")

    def announce_teardown(self):
        print(f"[Ephemeral teardown has completed at: {self._get_datetime_now()}]")

    @staticmethod
    def print_in_color(color: Fore, message: str) -> None:
        print(f"{color} {message} {Fore.RESET}")
