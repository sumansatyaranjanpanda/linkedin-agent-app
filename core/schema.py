from typing_extensions import TypedDict, NotRequired
import re
from typing import Literal

def _strip_think(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()


class NewsItem(TypedDict, total=False):
    title: NotRequired[str]
    url: str
    content: str
    score: float

class State(TypedDict, total=False):
    industry: str
    trending_news: list[NewsItem]
    summarize: str
    generator: str
    review_result: NotRequired[Literal["pass","fail"]]
    review_feedback: NotRequired[str]