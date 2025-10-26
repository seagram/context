import click
import keyring


@click.command()
def auth() -> None:
    """Prompts user to enter ChromaDB credentials"""
    existing_key: str | None = keyring.get_password("cortex", "chroma_api_key")
    if existing_key:
        masked_key: str = "*" * 6 + existing_key[-6:]
        if not click.confirm(
            f"Existing key ({masked_key}) found. Overwrite?", default=False
        ):
            click.echo("✓ Keeping existing credentials")
            return
    api_key = click.prompt("Enter your ChromaDB API Key", hide_input=True)
    keyring.set_password("cortex", "chroma_api_key", api_key)
    click.echo("✓ Credentials saved")
