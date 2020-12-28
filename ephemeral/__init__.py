"""Top-level package for ephemeral."""

__author__ = """Simon Kerr"""
__email__ = "jackofspaces@gmail.com"
__version__ = "0.1.0"

import colorama
import pluggy

from .configuration import Configuration

colorama.init()
NAME = "Ephemeral"

empheral_hookspec = pluggy.HookspecMarker(NAME)
empheral_hookimpl = pluggy.HookimplMarker(NAME)

__all__ = ["Configuration", "NAME", "empheral_hookspec", "empheral_hookimpl"]
