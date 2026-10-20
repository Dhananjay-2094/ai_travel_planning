import os
import requests

from tavily import TavilyClient

from dotenv import load_dotenv
load_dotenv()

client = TavilyClient(
    api_key = os.getenv("TAVILY_API_KEY")
)

def tavily_search(query):
    response = client.search(query=query, max_results=5)
    results = []
    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()
        # limiting to 300 charactes
        print("snippt : ",snippet)

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" " ,1)[0] + "..."
        results.append(f"{1}. **{title}**\n {url}\n {snippet}")
    return "\n\n".join(results)


