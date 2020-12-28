import argparse
from typing import Mapping

import pluggy

from .terminal_writer import TerminalWriter


class Configuration:
    def __init__(
        self, commandline_args: argparse.Namespace, plugin_manager: pluggy.PluginManager
    ) -> None:
        self.commandline_args: Mapping[str, str] = vars(commandline_args)
        self.terminal_writer = TerminalWriter(self.commandline_args)
        self.plugin_manager = plugin_manager
        self.verbose = self.commandline_args.get("verbose")
