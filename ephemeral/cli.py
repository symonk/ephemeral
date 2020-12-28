"""Console script for ephemeral."""
import argparse
import sys


def main():
    """Console script for ephemeral."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", action="store", required=True, destination="target")
    return 0


def ascii() -> None:
    ...


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
