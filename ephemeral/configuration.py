import argparse
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import Union

import pluggy

from .terminal_writer import TerminalWriter


class Configuration:
    def __init__(
        self, commandline_args: argparse.Namespace, plugin_manager: pluggy.PluginManager
    ) -> None:
        self.commandline_args: Mapping[str, Union[str, bool]] = vars(commandline_args)
        self.terminal_writer = TerminalWriter(self.commandline_args)
        self.plugin_manager = plugin_manager
        self.verbose: Optional[bool] = self.commandline_args.get("verbose")
        self.target: Optional[bool] = self.commandline_args.get("target")
        # 2 ** 16 (tcp port cap including registered & non registered).
        self.port_range: Iterable[int] = self.commandline_args.get(
            "port_range", range(65535 + 1)
        )
        self.quick: Optional[bool] = self.commandline_args.get("quick")
        self.random: Optional[bool] = self.commandline_args.get("random")
        self.thread_count: Optional[int] = self.commandline_args.get("thread_count")
