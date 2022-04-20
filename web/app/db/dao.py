from tortoise import Tortoise

from app.db.models import Article
from app.api.api_models import ArticleApiModel
from app.db.services import str_to_datetime


# Data Access Objects


async def is_article_async(article_id: str) -> bool:
    """_summary_ Check if article is present in DB

    bool: true -> article found in article table
    """
    found = await Article.filter(article_id=article_id).first()
    await Tortoise.close_connections()
    return bool(found)


async def read_article_from_db_async(article_id: str) -> ArticleApiModel:
    """Reads afrticle from DB table, converto to ArticleApiModel shape"""
    article_db_shape = await Article.filter(article_id=article_id).first()
    await Tortoise.close_connections()
    return ArticleApiModel(
        article_id=article_db_shape.article_id,
        title=article_db_shape.title,
        content=article_db_shape.content,
        created_at=article_db_shape.created_at,
        comments_number=article_db_shape.comments_number,
        author_first_name=article_db_shape.author_first_name,
        author_last_name=article_db_shape.author_last_name,
    )


async def write_article_to_db_async(article: ArticleApiModel) -> None:
    """writes article to article DB table"""
    article_db = await Article.create(
        article_id=article.article_id,
        title=article.title,
        content=article.content,
        created_at=str_to_datetime(article.created_at),
        comments_number=int(article.comments_number),
        author_first_name=article.author_first_name,
        author_last_name=article.author_last_name,
    )
    await article_db.save()
    await Tortoise.close_connections()
