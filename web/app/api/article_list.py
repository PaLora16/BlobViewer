from typing import Any, List
import requests
from app.api.normalize_response import normalize
from app.api.api_models import ArticleListApiModel
from app.api.api_validation import list_articles_validate

from app import app


def manage_response(r: Any) -> List[ArticleListApiModel]:
    _list_data = normalize(r)
    _articles: List[ArticleListApiModel] = []
    for _data in _list_data:
        kwargs = {
            "article_id": _data["id"],
            "title": _data["title"],
            "author_first_name": _data["author"]["first_name"],
            "author_last_name": _data["author"]["last_name"],
        }

        list_articles_validate(kwargs)
        model = ArticleListApiModel(**kwargs)

        _articles.append(model)
    return _articles


def api_get_articles() -> List[ArticleListApiModel]:
    """
    Summary : Fill List of ArticleListApiModel from TestApi
    It makes a request to the `ARTICLES_URL`
    Validate shape of responded data
    Raises exception if data invalid
    :return: A list of ArticleListApiModel objects
    """

    _url = app.config.get("ARTICLES_URL")

    response = requests.get(_url)
    return manage_response(response)
