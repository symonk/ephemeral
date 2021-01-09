"""
These hookspecs are purposely vague; I have no idea what specs should be exposed to the client plugins (yet).
Arguments & names are heavily subject to change!
"""
import argparse
from typing import Optional
from typing import Sequence

import pluggy

from sonic import Configuration

sonic_hookspec = pluggy.HookspecMarker("sonic")
sonic_hookimpl = pluggy.HookimplMarker("sonic")


@sonic_hookspec
def sonic_add_options(parser: argparse.ArgumentParser) -> None:
    """
    Bolt on command line options for the plugin
    """


@sonic_hookspec
def sonic_setup(config: Configuration) -> None:
    """
    Run basic setup!
    """


@sonic_hookspec(firstresult=True)
def sonic_execute(config: Configuration) -> Sequence[Optional[int]]:
    """
    Run basic execution!
    """


@sonic_hookspec
def sonic_teardown(
    config: Configuration, vulnerable_ports: Sequence[Optional[int]]
) -> None:
    """
    Run basic teardown!
    """


@sonic_hookspec
def sonic_report(config: Configuration, ports: Sequence[Optional[int]]) -> None:
    """
    Report the data about open ports!
    """
