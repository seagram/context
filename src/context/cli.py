import click
from context.commands import (
    auth,
    configure,
    list,
    add,
    remove,
    sync,
    search,
    stats,
    clear,
    export,
)


@click.group()
def cli():
    pass


cli.add_command(auth.auth)
cli.add_command(configure.configure)
cli.add_command(list.list)
cli.add_command(add.add)
cli.add_command(remove.remove)
cli.add_command(sync.sync)
cli.add_command(search.search)
cli.add_command(stats.stats)
cli.add_command(clear.clear)
cli.add_command(export.export)

if __name__ == "__main__":
    cli()
