// Example usage of the Chuck Norris Jokes MCP server
// This script demonstrates how to use the MCP tools in your code

// Import the MCP client library (this is just for demonstration purposes)
// In a real application, you would use the appropriate MCP client library
const mcpClient = {
  callTool: async (serverName, toolName, args) => {
    console.log(`Calling tool ${toolName} on server ${serverName} with args:`, args);
    console.log("This is a simulation - in a real application, this would call the actual MCP server");
    
    // Simulate some example responses
    if (toolName === 'get_joke_categories') {
      return {
        content: [
          {
            type: 'text',
            text: 'Available Chuck Norris joke categories:\n\nanimal, career, celebrity, dev, explicit, fashion, food, history, money, movie, music, political, religion, science, sport, travel'
          }
        ]
      };
    } else if (toolName === 'get_random_joke') {
      let category = args.category ? ` from category "${args.category}"` : '';
      return {
        content: [
          {
            type: 'text',
            text: `Chuck Norris doesn't read books. He stares them down until he gets the information he wants.${category ? '\nCategories: ' + args.category : ''}\n\nJoke ID: abcd1234`
          }
        ]
      };
    } else if (toolName === 'search_jokes') {
      return {
        content: [
          {
            type: 'text',
            text: `Found 3 jokes matching "${args.query}":\n\nChuck Norris can write infinite recursion functions and have them return.\n\nChuck Norris's keyboard doesn't have a Ctrl key because nothing controls Chuck Norris.\n\nAll arrays Chuck Norris declares are of infinite size, because Chuck Norris knows no bounds.`
          }
        ]
      };
    }
    
    return {
      content: [
        {
          type: 'text',
          text: 'Example response'
        }
      ]
    };
  }
};

// Example 1: Get all joke categories
async function getCategories() {
  const result = await mcpClient.callTool(
    'chuck-norris-jokes',
    'get_joke_categories',
    {}
  );
  console.log("\nCategories Result:");
  console.log(result.content[0].text);
}

// Example 2: Get a random joke
async function getRandomJoke(category = null) {
  const args = category ? { category } : {};
  const result = await mcpClient.callTool(
    'chuck-norris-jokes',
    'get_random_joke',
    args
  );
  console.log("\nRandom Joke Result:");
  console.log(result.content[0].text);
}

// Example 3: Search for jokes
async function searchJokes(query) {
  const result = await mcpClient.callTool(
    'chuck-norris-jokes',
    'search_jokes',
    { query }
  );
  console.log("\nSearch Result:");
  console.log(result.content[0].text);
}

// Run the examples
async function runExamples() {
  console.log("=== Chuck Norris Jokes MCP Server Example Usage ===");
  
  await getCategories();
  await getRandomJoke();
  await getRandomJoke('dev');
  await searchJokes('computer');
  
  console.log("\n=== End of Examples ===");
}

runExamples().catch(console.error);
