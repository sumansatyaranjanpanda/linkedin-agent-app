from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from config.settings import GROQ_API_KEY, TAVILY_API_KEY


# LLM client
llm = ChatGroq(model="llama3-8b-8192")

# Tavily client
tavily = TavilySearchResults(max_results=5)