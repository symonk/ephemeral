from datetime import datetime
from typing import Mapping


class TerminalWriter:
    @staticmethod
    def setup(namespace: Mapping[str, str]) -> None:
        print(
            f"[Ephemeral setup started at: {datetime.now().strftime('%d-%m-%Y @ %H:%M:%S')}]"
        )
        for setting, value in namespace.items():
            print(f"**** [{setting} = {value}] *****")

    def _print_time_information(self) -> None:
        ...

    def teardown(self):
        ...

    def print_key_value(self):
        ...
