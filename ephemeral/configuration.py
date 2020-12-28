import argparse
from typing import Mapping

from .terminal_writer import TerminalWriter


class Configuration:
    def __init__(self, commandline_args: argparse.Namespace) -> None:
        self.commandline_args: Mapping[str, str] = vars(commandline_args)
        self.terminal_writer = TerminalWriter()

    def setup(self) -> None:
        print("------------------------------------------")
        self.terminal_writer.setup(self.commandline_args)
        print("------------------------------------------")

    def execute(self) -> None:
        ...

    def teardown(self) -> None:
        self.terminal_writer.teardown()
