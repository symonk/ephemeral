"""Console script for ephemeral."""
import argparse
import sys


def main():
    """Console script for ephemeral."""
    welcome()
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", action="store", required=True, dest="target")
    return 0


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
  Ephemeral: Powerful python port scanner
    """
    )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
