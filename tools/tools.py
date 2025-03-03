from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = ""  # Ensure LangSmith is disabled
# os.environ["TAVILY_API_KEY"]
def get_profile_url_tavily(name: str):
    """Search  for Linkedin or Twitter profile page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

def get_profile_url_tavily(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res
#print(get_profile_url_tavily("Nitish Kumar iit bombay thapar"))