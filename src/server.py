from fastmcp import FastMCP

mcp = FastMCP("cortex")

@mcp.tool()
def search_notes(query: str, n_results: int = 5) -> list[dict]:
    """ Semantic search across all indexed documents in ChromaDB """
    pass

@mcp.tool()
def list_sources() -> list[dict]:
    """ List all documents in the ChromaDB collection """
    pass

@mcp.tool()
def get_context_window(chunk_id: str, window_size: int = 2) -> dict:
    """ Retrieve a chunk alongside surrounding chunks for more context """
    pass

@mcp.tool()
def search_by_metadata(query: str, source_filter: str = None, n_results: int = 5) -> list[dict]:
    """ Search with optional filtering by source file or metadata """
    pass

@mcp.tool()
def get_collection_stats() -> dict:
    """ Get statistics like total chunks, sources, etc. about the indexed collection """
    pass