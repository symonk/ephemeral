from random import shuffle
from typing import List

import colorama

from .abc.base_classes import Attackable
from .abc.base_classes import Scanable
from .abc.base_classes import Writable
from .configuration import Configuration
from .constants import QUICK_PORTS
from .results import ScanResult
from .utility.string_utils import StringTemplate


class ZonicInstance:
    def __init__(
        self,
        config: Configuration,
        scannable: Scanable,
        attackable: Attackable,
        writable: Writable,
    ) -> None:
        self.config = config
        self.scannable = scannable
        self.attackable = attackable
        self.writable = writable
        self._welcome()

    @property
    def scannable_ports(self) -> List[int]:
        def sort_order_ports(randomize: bool) -> List[int]:
            ports = list(self.config.port_range)
            if randomize:
                shuffle(ports)
            return ports

        return (
            QUICK_PORTS
            if self.config.quick
            else sort_order_ports(self.config.irregular)
        )

    def _welcome(self) -> None:
        """
        Write the welcome colourised ASCII art to standard art
        """
        template = StringTemplate(
            message=r"""
{0} ================================================= {1}{2}
 ______     ______     __   __     __     ______
/\___  \   /\  __ \   /\ "-.\ \   /\ \   /\  ___\
\/_/  /__  \ \ \/\ \  \ \ \-.  \  \ \ \  \ \ \____
  /\_____\  \ \_____\  \ \_\\"\_\  \ \_\  \ \_____\
  \/_____/   \/_____/   \/_/ \/_/   \/_/   \/_____/
{3}""",
            colour_options=(
                colorama.Fore.BLUE,
                colorama.Fore.RESET,
                colorama.Fore.LIGHTYELLOW_EX,
                colorama.Fore.RESET,
            ),
        )
        self.write(template)

    def display_configuration(self) -> None:
        self.write(
            StringTemplate(
                "{0}={1}" * 50, colour_options=(colorama.Fore.BLUE, colorama.Fore.RESET)
            )
        )
        self.write(
            StringTemplate(
                "Zonic: Powerful python port scanner, https://github.com/symonk/zonic"
            )
        )
        for opt, val in self.config.__dict__.items():
            self.write(
                StringTemplate(
                    "    Option: {0}{1}{2} => {3}",
                    colour_options=(colorama.Fore.GREEN, opt, colorama.Fore.RESET, val),
                )
            )
        self.write(
            StringTemplate(
                "{0}={1}" * 50, colour_options=(colorama.Fore.BLUE, colorama.Fore.RESET)
            )
        )

    def perform_scan(self) -> List[ScanResult]:
        result_set: List[ScanResult] = self.scannable.scan_ports(self.scannable_ports)
        for result in result_set:
            self.write(
                StringTemplate(
                    "Port {0}{1}{2} is {3}vulnerable{4}",
                    (
                        colorama.Fore.RED,
                        str(result.port).ljust(5, " "),
                        colorama.Fore.RESET,
                        colorama.Fore.RED,
                        colorama.Fore.RESET,
                    ),
                )
            )
        return result_set

    def write(self, template: StringTemplate, flush: bool = True) -> None:
        self.writable.write(template=template, flush=flush)
