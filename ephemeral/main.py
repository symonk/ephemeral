"""Console script for ephemeral."""
import argparse
import sys

import pluggy
from colorama import Fore
from pluggy import PluginManager

from ephemeral import NAME
from ephemeral import Configuration
from ephemeral.hooks import hookspec


def main():
    """Console script for ephemeral."""
    welcome()
    plugin_manager = pluggy.PluginManager(NAME)
    plugin_manager.add_hookspecs(hookspec)

    # Get the built in 'core' plugins, note user defined plugins can implement their own functionality!

    ephemeral_config = Configuration(generate_arg_namespace(), plugin_manager)
    _register_core_plugins(plugin_manager)
    if ephemeral_config.verbose:
        for plugin in plugin_manager.get_plugins():
            print(f"Plugin Registered => {Fore.GREEN + plugin.__name__ + Fore.RESET}")
    plugin_manager.hook.setup(config=ephemeral_config)
    plugin_manager.hook.execute(config=ephemeral_config)
    plugin_manager.hook.teardown(config=ephemeral_config)
    return 0


def _register_core_plugins(plugin_manager: PluginManager) -> None:
    from ephemeral.core import ephemeral_execute
    from ephemeral.core import ephemeral_setup
    from ephemeral.core import ephemeral_teardown

    plugin_manager.register(ephemeral_setup)
    plugin_manager.register(ephemeral_execute)
    plugin_manager.register(ephemeral_teardown)


def generate_arg_namespace() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        action="store",
        help="The target host to inspect available ports of.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run ephemeral in verbose mode",
        dest="verbose",
    )
    args = parser.parse_args()
    if args.target is None:
        print(
            "Ephemeral will terminate early, no --target was provided, please pass one in."
        )
        sys.exit(1)
    return parser.parse_args()


def welcome() -> None:
    print(
        fr"""
 =================================================== {Fore.LIGHTBLUE_EX}
  _____       _                                   _
 | ____|_ __ | |__   ___ _ __ ___   ___ _ __ __ _| |
 |  _| | '_ \| '_ \ / _ \ '_ ` _ \ / _ \ '__/ _` | |
 | |___| |_) | | | |  __/ | | | | |  __/ | | (_| | |
 |_____| .__/|_| |_|\___|_| |_| |_|\___|_|  \__,_|_|
       |_|
 {Fore.RESET} =================================================== {Fore.WHITE}
  Ephemeral: Powerful python port scanner!
    """,
        Fore.RESET,
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
