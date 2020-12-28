"""Console script for ephemeral."""
import argparse
import sys

import pluggy
from colorama import Fore

from ephemeral import NAME
from ephemeral import Configuration
from ephemeral.hooks import hookspec


def main():
    """Console script for ephemeral."""
    welcome()
    pm = pluggy.PluginManager(NAME)
    pm.add_hookspecs(hookspec)

    # Get the built in 'core' plugins, note user defined plugins can implement their own functionality!

    ephemeral_config = Configuration(generate_arg_namespace())
    ephemeral_config.setup()
    ephemeral_config.execute()
    ephemeral_config.teardown()
    return 0


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
        action="count",
        default=0,
        help="Level of verbosity, 0 (default)...5",
        dest="verbosity",
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
