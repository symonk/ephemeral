from typing import Iterable
from typing import Optional

import pluggy


class Configuration:
    def __init__(
        self,
        verbose: bool,
        target: str,
        port_range: Optional[Iterable[int]],
        quick: bool,
        random: bool,
        thread_count: bool,
        plugin_manager: pluggy.PluginManager,
    ) -> None:
        self.verbose = verbose
        self.target = target
        self.port_range = port_range or range(0, 2 ** 16)
        self.quick = quick
        self.random = random
        self.thread_count = thread_count
        self.plugin_manager = plugin_manager
