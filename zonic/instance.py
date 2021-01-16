import colorama

from .abc.base_classes import Attackable
from .abc.base_classes import Scanable
from .abc.base_classes import Writable
from .configuration import Configuration
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
        self._scannable = scannable
        self._attackable = attackable
        self._writable = writable
        self._welcome()

    def _welcome(self) -> None:
        """
        Write the welcome colourised ASCII art to standard art
        """
        template = StringTemplate(
            message=r"""
        ===================================================== {0}
         ______     ______     __   __     __     ______
        /\___  \   /\  __ \   /\ "-.\ \   /\ \   /\  ___\
        \/_/  /__  \ \ \/\ \  \ \ \-.  \  \ \ \  \ \ \____
          /\_____\  \ \_____\  \ \_\\"\_\  \ \_\  \ \_____\
          \/_____/   \/_____/   \/_/ \/_/   \/_/   \/_____/


        {1}===================================================== {2}
         Zonic: Powerful python port scanner, https://github.com/symonk/zonic
            {3}""",
            colour_options=(
                colorama.Fore.LIGHTBLUE_EX,
                colorama.Fore.RESET,
                colorama.Fore.WHITE,
                colorama.Fore.RESET,
            ),
        )
        self.write(template)

    def execute(self) -> int:
        ...

    def scan(self) -> None:
        ...

    def attack(self) -> None:
        ...

    def write(self, template: StringTemplate, flush: bool = True) -> None:
        self._writable.write(template=template, flush=flush)
