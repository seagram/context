<div align="center">
  <h1>context</h1>
  <p>
    <strong>Chat with your notes. Give AI assistants instant access to all of your documents.</strong>
  </p>
</div>

## About

_**Context**_ is a CLI/MCP server that lets AI assistants access your documents instantly.

It works by chunking your documents into collections of tokens, generating vector embeddings, and storing the vectors in [ChromaDB](https://www.trychroma.com/).

Context exposes a MCP server that you can install within Claude Code, Cursor, or any other AI assistants, giving them instant access to your documents through [RAG (Retrieval Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation).
