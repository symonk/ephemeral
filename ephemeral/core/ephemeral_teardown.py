from typing import Optional
from typing import Sequence

from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl


@ephemeral_hookimpl
def ephemeral_teardown(config: Configuration) -> Sequence[Optional[int]]:
    config.terminal_writer.announce_teardown()
    return []
