from datetime import datetime
from typing import Mapping


class TerminalWriter:
    def announce_setup(self, namespace: Mapping[str, str]) -> None:
        print(f"[Ephemeral setup started at: {self._get_datetime_now()}]")
        for setting, value in namespace.items():
            print(f"**** [{setting} = {value}] *****")

    @staticmethod
    def _get_datetime_now() -> str:
        return datetime.now().strftime("%d-%m-%Y @ %H:%M:%S")

    @staticmethod
    def announce_execution() -> None:
        print("[Ephemeral execution has begun...")

    def announce_teardown(self):
        print(f"[Ephemeral teardown has completed at: {self._get_datetime_now()}]")
