import click
from commands import auth, configure, list, add, remove, sync, search, stats, clear, export

@click.group()
def cli():
    pass

cli.add_command(auth)
cli.add_command(configure)
cli.add_command(list)
cli.add_command(add)
cli.add_command(remove)
cli.add_command(sync)
cli.add_command(search)
cli.add_command(stats)
cli.add_command(clear)
cli.add_command(export)

if __name__ == "__main__":
    cli()
