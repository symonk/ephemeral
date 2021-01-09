"""
These hookspecs are purposely vague; I have no idea what specs should be exposed to the client plugins (yet).
Arguments & names are heavily subject to change!
"""
import argparse
from typing import Optional
from typing import Sequence

import pluggy

from zonic import Configuration

zonic_hookspec = pluggy.HookspecMarker("zonic")
zonic_hookimpl = pluggy.HookimplMarker("zonic")


@zonic_hookspec
def zonic_add_options(parser: argparse.ArgumentParser) -> None:
    """
    Bolt on command line options for the plugin
    """


@zonic_hookspec
def zonic_setup(config: Configuration) -> None:
    """
    Run basic setup!
    """


@zonic_hookspec(firstresult=True)
def zonic_execute(config: Configuration) -> Sequence[Optional[int]]:
    """
    Run basic execution!
    """


@zonic_hookspec
def zonic_teardown(
    config: Configuration, vulnerable_ports: Sequence[Optional[int]]
) -> None:
    """
    Run basic teardown!
    """


@zonic_hookspec
def zonic_report(config: Configuration, ports: Sequence[Optional[int]]) -> None:
    """
    Report the data about open ports!
    """
