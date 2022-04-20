# BL for retrieving articles and list of articles

from app.api.article_list import api_get_articles
from app.api.article_by_id import api_get_article_by_id
from app.db.dao import (
    is_article_async,
    read_article_from_db_async,
    write_article_to_db_async,
)
from app.api.api_models import ArticleListApiModel, ArticleApiModel
from typing import List

import asyncio


def articles() -> List[ArticleListApiModel]:
    """fetch articles from TestAPI"""
    try:
        articles: List[ArticleListApiModel] = api_get_articles()

    except Exception as e:
        print(e)
    else:
        return articles


def article_by_id(article_id: str) -> ArticleApiModel:
    """Summary : Print  on terminal article given id
    1. Check if article id is save in DB table -> fetch on
    2. Try to fetch article from TestApi
    3. Article not found -> error messages -> end
    4. return article for next presentation
    """
    try:
        # check  if article is in DB table
        if asyncio.run(is_article_async(article_id)):
            article = asyncio.run(read_article_from_db_async(article_id))
        else:
            # read article from API
            article = api_get_article_by_id(article_id)
            # Save article to DB cache for next reading
            asyncio.run(write_article_to_db_async(article))
    except Exception as e:
        print(e)
    else:
        return article
