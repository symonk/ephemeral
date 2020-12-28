from datetime import datetime
from typing import Mapping

from colorama import Fore


class TerminalWriter:
    def __init__(self, options: Mapping[str, str]) -> None:
        self.options = options

    def announce_setup(self) -> None:
        print(f"**** Ephemeral setup started at: {self._get_datetime_now()}")
        for setting, value in self.options.items():
            print(
                f"**** [{Fore.BLUE + setting + Fore.RESET} = {Fore.GREEN + str(value) + Fore.RESET}] *****"
            )

    @staticmethod
    def _get_datetime_now() -> str:
        return datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")

    def announce_execute(self) -> None:
        print(f"**** Ephemeral Execution stage... : {self._get_datetime_now()}")

    def announce_teardown(self):
        print(f"**** Ephemeral teardown stage... : {self._get_datetime_now()}")

    def announce_report(self):
        print(f"Ephemeral reporting stage... {self._get_datetime_now()}]")

    @staticmethod
    def print_in_color(color: Fore, message: str) -> None:
        print(f"{color} {message} {Fore.RESET}")
