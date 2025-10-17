from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

# Load environment variables
load_dotenv()

# Create an MCP server
mcp = FastMCP("Perigon-News")

BASE_URL = "https://api.perigon.io/v1"

def make_perigon_request(endpoint: str, params: Dict = None) -> Any:
    """Helper function to make Perigon API requests"""
    api_key = os.getenv('PERIGON_API_KEY')
    if params is None:
        params = {}
    params['apiKey'] = api_key
    
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@mcp.tool()
def search_articles(query: str, size: int = 10, source: str = None, category: str = None) -> Dict:
    """
    Search for news articles with advanced filtering.
    
    Args:
        query (str): Search keywords (e.g., 'artificial intelligence', 'climate change')
        size (int): Number of results (1-100). Defaults to 10
        source (str): Filter by source domain (e.g., 'cnn.com', 'bbc.com')
        category (str): Filter by category (e.g., 'tech', 'business', 'sports')
    
    Returns:
        Dict: Articles with title, description, content, URL, and metadata
    
    Example: search_articles("bitcoin", size=5, category="business")
    """
    params = {
        "q": query,
        "size": min(size, 100)
    }
    if source:
        params["source"] = source
    if category:
        params["category"] = category
    
    return make_perigon_request("all", params)

@mcp.tool()
def get_top_headlines(country: str = "us", category: str = None, size: int = 10) -> Dict:
    """
    Get top headlines from a specific country.
    
    Args:
        country (str): 2-letter country code (us, uk, ca, au, in, etc.). Defaults to 'us'
        category (str): News category (tech, business, sports, politics, etc.)
        size (int): Number of headlines (1-100). Defaults to 10
    
    Returns:
        Dict: Top news articles with full metadata
    
    Example: get_top_headlines("uk", "technology", 5)
    """
    params = {
        "country": country,
        "size": min(size, 100),
        "sortBy": "date"
    }
    if category:
        params["category"] = category
    
    return make_perigon_request("all", params)

@mcp.tool()
def search_stories(query: str, size: int = 10) -> Dict:
    """
    Search for story clusters - groups of related articles about the same event.
    
    Args:
        query (str): Search keywords
        size (int): Number of story clusters (1-100). Defaults to 10
    
    Returns:
        Dict: Story clusters with article counts and aggregate data
    
    Example: search_stories("tesla stock", 5)
    """
    params = {
        "q": query,
        "size": min(size, 100)
    }
    return make_perigon_request("stories", params)

@mcp.tool()
def get_articles_by_date(query: str, from_date: str, to_date: str = None, size: int = 10) -> Dict:
    """
    Get articles within a specific date range.
    
    Args:
        query (str): Search keywords
        from_date (str): Start date in YYYY-MM-DD format (e.g., '2025-10-01')
        to_date (str): End date in YYYY-MM-DD format. Defaults to today
        size (int): Number of results (1-100). Defaults to 10
    
    Returns:
        Dict: Articles from the specified date range
    
    Example: get_articles_by_date("microsoft", "2025-10-01", "2025-10-15")
    """
    params = {
        "q": query,
        "from": from_date,
        "size": min(size, 100)
    }
    if to_date:
        params["to"] = to_date
    
    return make_perigon_request("all", params)

@mcp.tool()
def get_articles_by_source(source: str, size: int = 10) -> Dict:
    """
    Get latest articles from a specific news source.
    
    Args:
        source (str): Source domain (e.g., 'cnn.com', 'techcrunch.com', 'reuters.com')
        size (int): Number of articles (1-100). Defaults to 10
    
    Returns:
        Dict: Latest articles from the specified source
    
    Example: get_articles_by_source("bbc.com", 20)
    """
    params = {
        "source": source,
        "size": min(size, 100),
        "sortBy": "date"
    }
    return make_perigon_request("all", params)

@mcp.tool()
def search_with_sentiment(query: str, sentiment: str, size: int = 10) -> Dict:
    """
    Search for articles filtered by sentiment.
    
    Args:
        query (str): Search keywords
        sentiment (str): Sentiment filter ('positive', 'negative', 'neutral')
        size (int): Number of results (1-100). Defaults to 10
    
    Returns:
        Dict: Articles matching the sentiment criteria
    
    Example: search_with_sentiment("stock market", "positive", 10)
    """
    params = {
        "q": query,
        "sentiment": sentiment,
        "size": min(size, 100)
    }
    return make_perigon_request("all", params)

@mcp.tool()
def get_trending_topics(category: str = None, country: str = "us") -> Dict:
    """
    Get currently trending topics and news.
    
    Args:
        category (str): Filter by category (tech, business, sports, etc.)
        country (str): 2-letter country code. Defaults to 'us'
    
    Returns:
        Dict: Trending topics with article counts
    
    Example: get_trending_topics("technology", "us")
    """
    params = {
        "country": country,
        "sortBy": "relevance",
        "size": 20
    }
    if category:
        params["category"] = category
    
    return make_perigon_request("all", params)

if __name__ == "__main__":
    mcp.run(transport='stdio')