from app.controllers import articles, article_by_id
from app.api.api_models import ArticleListApiModel, ArticleApiModel
from typing import List
from tabulate import tabulate

# Presentation layer: formatted output to stdout
# - directly connetted to CLI command


def articles_to_stdout():
    # get list of articles
    list_articles: List[ArticleListApiModel] = articles()
    if list_articles:
        print_articles(list_articles)


def article_by_id_to_stdout(article_id: str):
    article: ArticleApiModel = article_by_id(article_id)
    if article:
        print_article(article)


# Helper function for printing content of articles on stdout
def print_articles(articles: List[ArticleListApiModel]) -> None:
    list_to_display = list(map(transform_list_article, articles))
    print(
        tabulate(
            list_to_display,
            headers=[
                "article id",
                "title",
                "author first_name",
                "author last name",
            ],
        )
    )


def transform_list_article(item: ArticleListApiModel) -> List[str]:
    """
    Helper function transformin content ArticleListApiModel class into List of items
    Reguirement of tabulate
    """
    return [item.article_id, item.title, item.author_first_name, item.author_last_name]


# Helper functions
def print_article(article: ArticleApiModel) -> None:
    """_summary_ print article items on stout

    Args:
        article (ArticleApiModel): _description_
    """
    print(f"ARTICLE ID  : {article.article_id}")
    print(f"TITLE : {article.title}")
    print(f"CONTENT : {article.content}")
    print(f"CREATED at : {article.created_at}")
    print(f"COMMENTS NUMBER : {article.comments_number}")
    print(f"AUTHOR FIRST NAME : {article.author_first_name}")
    print(f"AUTHOR LAST NAME : {article.author_last_name}")
