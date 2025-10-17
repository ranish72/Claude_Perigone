\# Perigon MCP Server for Claude



Access real-time, AI-enriched global news data from 195,000+ sources using Perigon API with Claude Desktop.



\## 🌟 Features



\- \*\*Real-time News\*\* - Articles available within 1-5 minutes of publication

\- \*\*AI-Enhanced Data\*\* - Sentiment analysis, entity extraction, content clustering

\- \*\*Story Clustering\*\* - Groups related articles about the same event

\- \*\*Advanced Search\*\* - Filter by source, category, country, date range, sentiment

\- \*\*195,000+ Sources\*\* - Comprehensive global news coverage

\- \*\*Trending Topics\*\* - Discover what's making headlines right now



\## 📊 Why Perigon?



| Feature | Perigon | Others |

|---------|---------|--------|

| Sources | 195,000+ | ~80,000 |

| AI Enhancement | ✅ Full | ❌ Limited |

| Story Clustering | ✅ Yes | ❌ No |

| Latency | 1-5 min | 24 hours |

| Sentiment Analysis | ✅ Yes | ❌ No |



\## 🚀 Setup



\### 1. Clone this repository

```bash

git clone https://github.com/YOUR\_USERNAME/Claude-Perigon-MCP.git

cd Claude-Perigon-MCP

```



\### 2. Get your API key

Get your API key from \[Perigon.io](https://www.perigon.io/)



\### 3. Create `.env` file

```bash

PERIGON\_API\_KEY=your\_api\_key\_here

```



\### 4. Install dependencies

```bash

uv add mcp requests python-dotenv

```



\## ⚙️ Claude Desktop Configuration



Add to `claude\_desktop\_config.json`:



\### Windows

```json

{

&nbsp; "mcpServers": {

&nbsp;   "perigon-news": {

&nbsp;     "command": "C:\\\\Users\\\\YOUR\_USERNAME\\\\.local\\\\bin\\\\uv.exe",

&nbsp;     "args": \[

&nbsp;       "--directory",

&nbsp;       "C:\\\\path\\\\to\\\\Claude\_Perigon",

&nbsp;       "run",

&nbsp;       "main.py"

&nbsp;     ]

&nbsp;   }

&nbsp; }

}

```



\### macOS/Linux

```json

{

&nbsp; "mcpServers": {

&nbsp;   "perigon-news": {

&nbsp;     "command": "uv",

&nbsp;     "args": \[

&nbsp;       "--directory",

&nbsp;       "/path/to/Claude\_Perigon",

&nbsp;       "run",

&nbsp;       "main.py"

&nbsp;     ]

&nbsp;   }

&nbsp; }

}

```



\## 🎯 Available Tools



\### 1. \*\*search\_articles\*\*

Search for news articles with advanced filtering

```

Args:

\- query (str): Search keywords

\- size (int): Number of results (1-100)

\- source (str): Filter by source domain

\- category (str): Filter by category

```



\### 2. \*\*get\_top\_headlines\*\*

Get top headlines from a specific country

```

Args:

\- country (str): 2-letter country code (us, uk, ca, etc.)

\- category (str): News category

\- size (int): Number of headlines

```



\### 3. \*\*search\_stories\*\*

Search for story clusters - groups of related articles

```

Args:

\- query (str): Search keywords

\- size (int): Number of story clusters

```



\### 4. \*\*get\_articles\_by\_date\*\*

Get articles within a specific date range

```

Args:

\- query (str): Search keywords

\- from\_date (str): Start date (YYYY-MM-DD)

\- to\_date (str): End date (YYYY-MM-DD)

\- size (int): Number of results

```



\### 5. \*\*get\_articles\_by\_source\*\*

Get latest articles from a specific news source

```

Args:

\- source (str): Source domain (e.g., 'cnn.com')

\- size (int): Number of articles

```



\### 6. \*\*search\_with\_sentiment\*\*

Search for articles filtered by sentiment

```

Args:

\- query (str): Search keywords

\- sentiment (str): 'positive', 'negative', or 'neutral'

\- size (int): Number of results

```



\### 7. \*\*get\_trending\_topics\*\*

Get currently trending topics and news

```

Args:

\- category (str): Filter by category

\- country (str): 2-letter country code

```



\## 💬 Usage Examples



Ask Claude:

\- "Search for AI news using Perigon"

\- "Get top technology headlines from the UK"

\- "Find positive sentiment articles about Tesla from this week"

\- "Show me story clusters about climate change"

\- "Get latest articles from TechCrunch"

\- "What are the trending business topics in the US today?"

\- "Search for articles about SpaceX from October 2025"



\## 📝 API Endpoint



The server uses Perigon's REST API:

```

https://api.perigon.io/v1/all

```



\## 🔐 Security



\- \*\*NEVER\*\* commit your `.env` file to Git

\- The `.gitignore` file protects your API key

\- Keep your API credentials secure



\## 🛠️ Tech Stack



\- \*\*Python\*\* - Core language

\- \*\*FastMCP\*\* - MCP server framework

\- \*\*requests\*\* - HTTP library

\- \*\*python-dotenv\*\* - Environment variable management

\- \*\*uv\*\* - Fast Python package manager



\## 📚 Dependencies

```toml

\[project]

dependencies = \[

&nbsp;   "mcp",

&nbsp;   "requests",

&nbsp;   "python-dotenv"

]

```



\## 🐛 Troubleshooting



\### Server won't start

\- Check that `.env` file exists with valid API key

\- Verify `uv` is installed: `uv --version`

\- Ensure all dependencies installed: `uv pip list`



\### EOF Error during local test

\- \*\*This is normal!\*\* The server expects JSON-RPC input

\- The real test is in Claude Desktop, not terminal

\- Just press Ctrl+C and proceed with Claude integration



\### Claude doesn't see the tool

\- Restart Claude Desktop completely (not just close window)

\- Verify path in `claude\_desktop\_config.json` is absolute

\- Check that server name doesn't conflict with existing servers



\## 📖 Documentation



\- \[Perigon API Docs](https://docs.perigon.io/)

\- \[MCP Protocol](https://modelcontextprotocol.io/)

\- \[FastMCP Documentation](https://github.com/jlowin/fastmcp)



\## 🤝 Contributing



Contributions welcome! Please:

1\. Fork the repository

2\. Create a feature branch

3\. Make your changes

4\. Submit a pull request



\## 📄 License



MIT License - feel free to use and modify



\## 🙏 Acknowledgments



\- Built with \[Perigon API](https://www.perigon.io/)

\- Powered by \[MCP Protocol](https://modelcontextprotocol.io/)

\- Uses \[FastMCP](https://github.com/jlowin/fastmcp) framework



\## 📞 Support



\- \*\*Perigon API Issues\*\*: \[email protected]

\- \*\*MCP Questions\*\*: \[MCP Discord](https://discord.gg/anthropic)

\- \*\*Project Issues\*\*: Open a GitHub issue



---



\*\*Note\*\*: This is a local MCP server implementation. Perigon also offers a remote MCP server at `https://mcp.perigon.io/v1/sse` if you prefer a hosted solution.



\## 🎉 Happy News Hunting!



Made with ❤️ for the Claude Desktop community

