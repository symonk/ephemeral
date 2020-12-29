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
    welcome()
    plugin_manager = pluggy.PluginManager(NAME)
    plugin_manager.add_hookspecs(hookspec)
    ephemeral_config = generate_config_dict(plugin_manager)
    _register_core_plugins(ephemeral_config, plugin_manager)
    plugin_manager.hook.ephemeral_setup(config=ephemeral_config)
    ports = plugin_manager.hook.ephemeral_execute(config=ephemeral_config)
    plugin_manager.hook.ephemeral_teardown(
        config=ephemeral_config, vulnerable_ports=ports
    )
    plugin_manager.hook.ephemeral_report(config=ephemeral_config, ports=ports)
    return 0


def _register_core_plugins(
    config: Configuration, plugin_manager: PluginManager
) -> None:
    from ephemeral.core.ephemeral_core import EphemeralCorePlugin
    from ephemeral.core.ephemeral_csv import EphemeralCSVPlugin

    core_plugin = EphemeralCorePlugin(config, plugin_manager)
    csv_plugin = EphemeralCSVPlugin(config, plugin_manager)
    plugin_manager.register(plugin=core_plugin, name=core_plugin.name)
    plugin_manager.register(plugin=csv_plugin, name=csv_plugin.name)


def generate_config_dict(plugin_manager: PluginManager) -> Configuration:
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
        default=5_000,
        help="How many threads should scanning use, this depends heavily on available memory, tweak accordingly.",
        dest="thread_count",
    )
    parser.add_argument(
        "--pr",
        "--ports",
        action="store",
        type=int,
        default=None,
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

    namespace = parser.parse_args()
    keyword_args = vars(namespace)
    keyword_args["plugin_manager"] = plugin_manager
    config = Configuration(**keyword_args)
    return config


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
