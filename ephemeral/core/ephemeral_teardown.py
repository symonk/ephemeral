from ephemeral import Configuration
from ephemeral import empheral_hookimpl


@empheral_hookimpl
def teardown(config: Configuration) -> None:
    config.terminal_writer.announce_teardown()
