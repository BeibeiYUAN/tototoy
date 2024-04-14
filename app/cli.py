"""Console script for tototoy."""

import sys

import click


@click.command()
def main(args=None):
    """Console script for tototoy."""
    click.echo("Replace this message by putting your code into " "tototoy.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
