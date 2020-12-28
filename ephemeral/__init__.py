"""Top-level package for ephemeral."""

__author__ = """Simon Kerr"""
__email__ = "jackofspaces@gmail.com"
__version__ = "0.1.0"

import colorama
import pluggy

from .configuration import Configuration

colorama.init()
NAME = "Ephemeral"

ephemeral_hookspec = pluggy.HookspecMarker(NAME)
ephemeral_hookimpl = pluggy.HookimplMarker(NAME)

__all__ = ["Configuration", "NAME", "ephemeral_hookspec", "ephemeral_hookimpl"]
