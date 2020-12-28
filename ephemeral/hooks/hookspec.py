"""
These hookspecs are purposely vague; I have no idea what specs should be exposed to the client plugins (yet).
Arguments & names are heavily subject to change!
"""
from ephemeral import Configuration
from ephemeral import empheral_hookspec


@empheral_hookspec
def setup(config: Configuration) -> None:
    """
    Run basic setup!
    """


@empheral_hookspec
def execute(config: Configuration) -> None:
    """
    Run basic execution!
    """


@empheral_hookspec
def teardown(config: Configuration) -> None:
    """
    Run basic teardown!
    """
