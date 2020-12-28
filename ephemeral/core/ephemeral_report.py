from typing import Optional
from typing import Sequence

from colorama import Fore

from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl


@ephemeral_hookimpl
def ephemeral_report(config: Configuration, ports: Sequence[Optional[int]]) -> None:
    config.terminal_writer.announce_report()
    for port in ports:
        print(
            f" **** Port: {Fore.GREEN + str(port) + Fore.RESET} is potentially {Fore.RED} vulnerable! {Fore.RESET}"
        )
