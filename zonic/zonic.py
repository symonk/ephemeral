"""Console script for zonic."""
import argparse
import sys

import colorama

from .configuration import Configuration
from .impl import Attacker
from .impl import Scanner
from .impl import Writer
from .instance import ZonicInstance


def parse_sysargv() -> argparse.Namespace:
    """
    Parses sys.argv via the argparse module.
    store_true | store_false are implicit in their values, however we are explicit here.
    :return: The argparse.Namespace instance from `parse_args()`
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        action="store",
        required=True,
        help="The target host to inspect available ports of.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run zonic in verbose mode",
        dest="verbose",
        default=False,
    )
    parser.add_argument(
        "-q",
        "--quick",
        action="store_true",
        help="Scan only the top 100 popular open ports",
        dest="quick",
    )
    parser.add_argument(
        "-i",
        "--irregular",
        action="store_true",
        help="Scan ports in the port range randomly, not sequentially.",
        dest="irregular",
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
        "-csv",
        "--csv-output",
        action="store_true",
        default=False,
        help="If vulnerable ports are detected; write them to csv in the cwd",
        dest="csv_output",
    )
    return parser.parse_args()


def main():
    colorama.init()
    namespace = parse_sysargv()
    config = Configuration(**vars(namespace))
    scanner = Scanner(config)
    attacker = Attacker()
    zonic = ZonicInstance(
        config=config, scannable=scanner, attackable=attacker, writable=Writer()
    )
    zonic.attack()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
