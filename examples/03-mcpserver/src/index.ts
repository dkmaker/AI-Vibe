#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import axios from 'axios';

// Chuck Norris API base URL
const API_BASE_URL = 'https://api.chucknorris.io/jokes';

// Interface for Chuck Norris joke response
interface ChuckNorrisJoke {
  id: string;
  value: string;
  url: string;
  icon_url: string;
  created_at: string;
  updated_at: string;
  categories: string[];
}

// Interface for categories response
interface CategoriesResponse {
  categories: string[];
}

class ChuckNorrisJokesServer {
  private server: Server;
  private axiosInstance;

  constructor() {
    this.server = new Server(
      {
        name: 'chuck-norris-jokes-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.axiosInstance = axios.create({
      baseURL: API_BASE_URL,
    });

    this.setupToolHandlers();
    
    // Error handling
    this.server.onerror = (error) => console.error('[MCP Error]', error);
    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'get_joke_categories',
          description: 'Get all available Chuck Norris joke categories',
          inputSchema: {
            type: 'object',
            properties: {},
            required: [],
          },
        },
        {
          name: 'get_random_joke',
          description: 'Get a random Chuck Norris joke',
          inputSchema: {
            type: 'object',
            properties: {
              category: {
                type: 'string',
                description: 'Optional category to filter jokes by',
              },
            },
            required: [],
          },
        },
        {
          name: 'get_joke_by_id',
          description: 'Get a specific Chuck Norris joke by its ID',
          inputSchema: {
            type: 'object',
            properties: {
              id: {
                type: 'string',
                description: 'The ID of the joke to retrieve',
              },
            },
            required: ['id'],
          },
        },
        {
          name: 'search_jokes',
          description: 'Search for Chuck Norris jokes containing specific text',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'The text to search for in jokes',
              },
            },
            required: ['query'],
          },
        }
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      try {
        switch (request.params.name) {
          case 'get_joke_categories':
            return await this.getJokeCategories();
          case 'get_random_joke':
            return await this.getRandomJoke(request.params.arguments);
          case 'get_joke_by_id':
            return await this.getJokeById(request.params.arguments);
          case 'search_jokes':
            return await this.searchJokes(request.params.arguments);
          default:
            throw new McpError(
              ErrorCode.MethodNotFound,
              `Unknown tool: ${request.params.name}`
            );
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          return {
            content: [
              {
                type: 'text',
                text: `Chuck Norris API error: ${
                  error.response?.data?.message || error.message
                }`,
              },
            ],
            isError: true,
          };
        }
        throw error;
      }
    });
  }

  private async getJokeCategories() {
    try {
      const response = await this.axiosInstance.get<string[]>('/categories');
      return {
        content: [
          {
            type: 'text',
            text: `Available Chuck Norris joke categories:\n\n${response.data.join(', ')}`,
          },
        ],
      };
    } catch (error) {
      console.error('Error fetching categories:', error);
      throw error;
    }
  }

  private async getRandomJoke(args: any) {
    try {
      let endpoint = '/random';
      if (args?.category) {
        endpoint = `/random?category=${encodeURIComponent(args.category)}`;
      }
      
      const response = await this.axiosInstance.get<ChuckNorrisJoke>(endpoint);
      const joke = response.data;
      
      let categoryInfo = '';
      if (joke.categories && joke.categories.length > 0) {
        categoryInfo = `\nCategories: ${joke.categories.join(', ')}`;
      }
      
      return {
        content: [
          {
            type: 'text',
            text: `${joke.value}${categoryInfo}\n\nJoke ID: ${joke.id}`,
          },
        ],
      };
    } catch (error) {
      console.error('Error fetching random joke:', error);
      throw error;
    }
  }

  private async getJokeById(args: any) {
    if (!args?.id) {
      throw new McpError(
        ErrorCode.InvalidParams,
        'Joke ID is required'
      );
    }

    try {
      const response = await this.axiosInstance.get<ChuckNorrisJoke>(`/${args.id}`);
      const joke = response.data;
      
      let categoryInfo = '';
      if (joke.categories && joke.categories.length > 0) {
        categoryInfo = `\nCategories: ${joke.categories.join(', ')}`;
      }
      
      return {
        content: [
          {
            type: 'text',
            text: `${joke.value}${categoryInfo}\n\nJoke ID: ${joke.id}`,
          },
        ],
      };
    } catch (error) {
      console.error('Error fetching joke by ID:', error);
      throw error;
    }
  }

  private async searchJokes(args: any) {
    if (!args?.query) {
      throw new McpError(
        ErrorCode.InvalidParams,
        'Search query is required'
      );
    }

    if (args.query.length < 3) {
      return {
        content: [
          {
            type: 'text',
            text: 'Search query must be at least 3 characters long',
          },
        ],
        isError: true,
      };
    }

    try {
      const response = await this.axiosInstance.get<{total: number, result: ChuckNorrisJoke[]}>(`/search?query=${encodeURIComponent(args.query)}`);
      
      if (response.data.total === 0) {
        return {
          content: [
            {
              type: 'text',
              text: `No jokes found matching "${args.query}"`,
            },
          ],
        };
      }
      
      const jokes = response.data.result.map(joke => joke.value);
      
      return {
        content: [
          {
            type: 'text',
            text: `Found ${response.data.total} jokes matching "${args.query}":\n\n${jokes.join('\n\n')}`,
          },
        ],
      };
    } catch (error) {
      console.error('Error searching jokes:', error);
      throw error;
    }
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Chuck Norris Jokes MCP server running on stdio');
  }
}

const server = new ChuckNorrisJokesServer();
server.run().catch(console.error);
