import datetime
from dataclasses import dataclass


@dataclass
class ArticleApiModel:
    """Article flattened data from API"""

    article_id: str
    title: str
    content: str
    created_at: datetime
    comments_number: int
    author_first_name: str
    author_last_name: str


@dataclass
class ArticleListApiModel:
    """Articles flattened data from API"""

    article_id: str
    title: str
    author_first_name: str
    author_last_name: str
