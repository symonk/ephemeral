"""
These hookspecs are purposely vague; I have no idea what specs should be exposed to the client plugins (yet).
Arguments & names are heavily subject to change!
"""
from typing import List
from typing import Optional

from ephemeral import Configuration
from ephemeral import ephemeral_hookspec


@ephemeral_hookspec
def ephemeral_setup(config: Configuration) -> None:
    """
    Run basic setup!
    """


@ephemeral_hookspec(firstresult=True)
def ephemeral_execute(config: Configuration) -> List[Optional[int]]:
    """
    Run basic execution!
    """


@ephemeral_hookspec
def ephemeral_teardown(config: Configuration, ports: List[Optional[int]]) -> None:
    """
    Run basic teardown!
    """


@ephemeral_hookspec
def ephemeral_report(config: Configuration, ports: List[Optional[int]]) -> None:
    """
    Report the data about open ports!
    """