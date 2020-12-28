"""Console script for ephemeral."""
import argparse
import sys

from ephemeral import Configuration


def main():
    """Console script for ephemeral."""
    welcome()
    ephemeral_config = Configuration(generate_arg_namespace())
    ephemeral_config.setup()

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
    return parser.parse_args()


def welcome() -> None:
    print(
        r"""
 ===================================================
  _____       _                                   _
 | ____|_ __ | |__   ___ _ __ ___   ___ _ __ __ _| |
 |  _| | '_ \| '_ \ / _ \ '_ ` _ \ / _ \ '__/ _` | |
 | |___| |_) | | | |  __/ | | | | |  __/ | | (_| | |
 |_____| .__/|_| |_|\___|_| |_| |_|\___|_|  \__,_|_|
       |_|
  ===================================================
  Ephemeral: Powerful python port scanner!
    """
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
