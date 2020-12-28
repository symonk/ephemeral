from ephemeral import Configuration
from ephemeral import ephemeral_hookimpl


@ephemeral_hookimpl
def ephemeral_setup(config: Configuration) -> None:
    config.terminal_writer.announce_setup()
