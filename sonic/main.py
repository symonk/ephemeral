"""Console script for sonic."""
import argparse
import sys

from colorama import Fore
from pluggy import PluginManager

from sonic import Configuration
from sonic import plugin_manager


def sonic_add_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--target",
        action="store",
        help="The target host to inspect available ports of.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run sonic in verbose mode",
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
        "-tc",
        "--thread-count",
        action="store",
        type=int,
        default=5_000,
        help="How many threads should scanning use, this depends heavily on available memory, tweak accordingly.",
        dest="thread_count",
    )
    parser.add_argument(
        "-pr",
        "--ports",
        action="store",
        type=int,
        default=range(65536),
        help="Specify the port range to perform a scan on.",
        dest="port_range",
    )
    parser.add_argument(
        "-wv",
        "--write-vulnerable",
        action="store_true",
        default=False,
        help="If vulnerable ports are detected; write them to csv in the cwd",
        dest="write_vulnerable",
    )


def main():
    welcome()
    parser = argparse.ArgumentParser()
    plugin_manager.register(__file__, "sonic_main")
    plugin_options = plugin_manager.hook.sonic_add_options(parser=parser)
    return 0


def _register_core_plugins(
    config: Configuration, plugin_manager: PluginManager
) -> None:
    from sonic.core.sonic_core import SonicCorePlugin
    from sonic.core.sonic_csv import SonicCSVPlugin

    core_plugin = SonicCorePlugin(config, plugin_manager)
    csv_plugin = SonicCSVPlugin(config, plugin_manager)
    plugin_manager.register(plugin=core_plugin, name=core_plugin.name)
    plugin_manager.register(plugin=csv_plugin, name=csv_plugin.name)


def welcome() -> None:
    print(
        fr"""
================================ {Fore.LIGHTBLUE_EX}
   _____             _
  / ___/____  ____  (_)____
  \__ \/ __ \/ __ \/ / ___/
 ___/ / /_/ / / / / / /__
/____/\____/_/ /_/_/\___/

{Fore.RESET} =================== {Fore.WHITE}
  sonic: Powerful python port scanner, https://github.com/symonk/sonic
    """,
        Fore.RESET,
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
