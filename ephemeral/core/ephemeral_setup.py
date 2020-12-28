from ephemeral import Configuration
from ephemeral import empheral_hookimpl


@empheral_hookimpl
def setup(config: Configuration) -> None:
    config.terminal_writer.announce_setup()
