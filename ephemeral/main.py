"""Console script for ephemeral."""
import argparse
import sys


def main():
    """Console script for ephemeral."""
    welcome()
    namespace = generate_arg_namespace()
    generate_namespace_output(namespace)
    return 0


def generate_arg_namespace() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target", action="store", help="The target host to inspect available ports of."
    )
    parser.add_argument(
        "-v", "--verbose", action="count", help="Level of verbosity, 0 (default)...5"
    )
    return parser.parse_args()


def generate_namespace_output(namespace: argparse.Namespace) -> None:
    for item in vars(namespace).values():
        print_kv(item)


def print_kv(arg_data: str) -> None:
    key, value = arg_data.split("=")
    print(f"**** [{key} = {value}] *****")


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
  Ephemeral: Powerful python port scanner, configuration summary is below:
    """
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
