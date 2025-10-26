import click

@click.command()
def auth():
    """ Prompts user to enter ChromaDB credentials """
    pass

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