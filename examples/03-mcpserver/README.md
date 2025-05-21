# Chuck Norris Jokes MCP Server

This is an example MCP (Model Context Protocol) server that provides tools for fetching Chuck Norris jokes from the [Chuck Norris API](https://api.chucknorris.io/).

## Features

- Get all available joke categories
- Get a random joke (optionally filtered by category)
- Get a specific joke by ID
- Search for jokes containing specific text

## Installation

1. Install dependencies:

```bash
cd examples/03-mcpserver
npm install
```

2. Build the server:

```bash
npm run build
```

## MCP Configuration

To add this server to your MCP configuration, add the following to your MCP settings file:

For VSCode Cline extension:
- Location: `%APPDATA%\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json`

```json
{
  "mcpServers": {
    "chuck-norris-jokes": {
      "command": "node",
      "args": ["C:/Code/DKMaker/AI-Vibe/examples/03-mcpserver/build/index.js"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Available Tools

### get_joke_categories

Get all available Chuck Norris joke categories.

Example:
```json
{
  "name": "get_joke_categories",
  "arguments": {}
}
```

### get_random_joke

Get a random Chuck Norris joke, optionally filtered by category.

Example:
```json
{
  "name": "get_random_joke",
  "arguments": {
    "category": "dev" // Optional
  }
}
```

### get_joke_by_id

Get a specific Chuck Norris joke by its ID.

Example:
```json
{
  "name": "get_joke_by_id",
  "arguments": {
    "id": "abc123" // Required
  }
}
```

### search_jokes

Search for Chuck Norris jokes containing specific text.

Example:
```json
{
  "name": "search_jokes",
  "arguments": {
    "query": "computer" // Required, minimum 3 characters
  }
}
```

## API Reference

This server uses the [Chuck Norris API](https://api.chucknorris.io/):

- `/jokes/categories` - Get all categories
- `/jokes/random` - Get a random joke
- `/jokes/random?category={category}` - Get a random joke from a specific category
- `/jokes/{id}` - Get a joke by ID
- `/jokes/search?query={query}` - Search for jokes
