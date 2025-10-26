import click
import keyring

@click.command()
def auth():
    """ Prompts user to enter ChromaDB credentials """
    existing_key = keyring.get_password("cortex", "chroma_api_key")
    if existing_key:
        masked_key = "*" * 6 + existing_key[-6:]
        if not click.confirm(f"Existing key ({masked_key}) found. Overwrite?", default=False):
            click.echo("✓ Keeping existing credentials")
            return
    api_key = click.prompt("Enter your ChromaDB API Key", hide_input=True)
    keyring.set_password("cortex", "chroma_api_key", api_key)
    click.echo("✓ Credentials saved")

@click.command()
def configure():
    """ Set up MCP server configuration for different tools """
    pass

@click.command()
def list():
    """ List all documents currently indexed in ChromaDB """
    pass

@click.command()
def add():
    """ Chunk and index document(s) from a file or directory to ChromaDB """
    pass

@click.command()
def remove():
    """ Delete document from ChromaDB """
    pass

@click.command()
def sync():
    """ Re-index document(s) to ChromaDB """
    pass

@click.command()
def search():
    """ Test a search query to preview a MCP server result """
    pass

@click.command()
def stats():
    """ Show total chunk count, documents uploaded, and other statistics from ChromaDB """
    pass

@click.command()
def clear():
    """ Delete entire ChromaDB collection """
    pass

@click.command()
def export():
    """ Export chunk metadata and documents to JSON """
    pass