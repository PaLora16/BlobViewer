from typing import Any
import requests
from app.api.normalize_response import normalize
from app.api.api_models import ArticleApiModel
from app.api.api_validation import article_validate

from app import app


def manage_response(r: Any) -> ArticleApiModel:
    """
    It takes response from API request, test formal validity
    and transform JSON response to dataclass article model
    :param r: Any - the response from the API
    :type r: Any
    """
    _data = normalize(r)

    article_validate(_data)

    return ArticleApiModel(
        article_id=_data["id"],
        title=_data["title"],
        content=_data["content"],
        created_at=_data["created_at"],
        comments_number=_data["comments"],
        author_first_name=_data["author"]["first_name"],
        author_last_name=_data["author"]["last_name"],
    )


def api_get_article_by_id(article_id: str) -> ArticleApiModel:
    _url = app.config.get("ARTICLE_BY_ID_URL") + article_id

    response = requests.get(_url)
    return manage_response(response)
