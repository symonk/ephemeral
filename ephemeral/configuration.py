import argparse
from typing import Mapping

from .decorators import stdout_separated
from .terminal_writer import TerminalWriter


class Configuration:
    def __init__(self, commandline_args: argparse.Namespace) -> None:
        self.commandline_args: Mapping[str, str] = vars(commandline_args)
        self.terminal_writer = TerminalWriter()

    @stdout_separated
    def setup(self) -> None:
        self.terminal_writer.announce_setup(self.commandline_args)

    @stdout_separated
    def execute(self) -> None:
        self.terminal_writer.announce_execution()

    @stdout_separated
    def teardown(self) -> None:
        self.terminal_writer.announce_teardown()
