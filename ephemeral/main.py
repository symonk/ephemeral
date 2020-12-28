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
    ephemeral_config = Configuration(generate_arg_namespace(), plugin_manager)
    _register_core_plugins(plugin_manager)
    if ephemeral_config.verbose:
        for plugin in plugin_manager.get_plugins():
            print(f"Plugin Registered => {Fore.GREEN + plugin.__name__ + Fore.RESET}")
    plugin_manager.hook.ephemeral_setup(config=ephemeral_config)
    ports = plugin_manager.hook.ephemeral_execute(config=ephemeral_config)
    plugin_manager.hook.ephemeral_teardown(config=ephemeral_config, ports=ports)
    plugin_manager.hook.ephemeral_report(config=ephemeral_config, ports=ports)
    return 0


def _register_core_plugins(plugin_manager: PluginManager) -> None:
    from ephemeral.core import ephemeral_execute
    from ephemeral.core import ephemeral_report
    from ephemeral.core import ephemeral_setup
    from ephemeral.core import ephemeral_teardown

    plugin_manager.register(ephemeral_setup)
    plugin_manager.register(ephemeral_execute)
    plugin_manager.register(ephemeral_teardown)
    plugin_manager.register(ephemeral_report)


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
    parser.add_argument(
        "-q",
        "--quick",
        action="store_true",
        help="Scan only the top 100 popular open ports",
        dest="quick",
    )
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="Scan ports in the port range randomly, not sequentially.",
        dest="random",
    )
    parser.add_argument(
        "--tc",
        "--thread-count",
        action="store",
        type=int,
        default=100,
        help="How many threads should scanning use, this depends heavily on available memory, tweak accordingly.",
        dest="thread_count",
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
  Ephemeral: Powerful python port scanner, https://github.com/symonk/ephemeral
    """,
        Fore.RESET,
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
