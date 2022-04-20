from marshmallow import Schema, fields


class ArticleSchema(Schema):

    id = fields.String(
        required=True, error_messages={"required": "article_id is required."}
    )

    title = fields.String(
        required=True, error_messages={"required": "title is required."}
    )
    content = fields.String(
        required=True, error_messages={"required": "content is required."}
    )
    created_at = fields.String()
    comments = fields.Int(
        required=True, error_messages={"required": "comments is required."}
    )
    author = fields.Dict(
        required=True, error_messages={"required": "author is required."}
    )


class ListArticlesSchema(Schema):
    article_id = fields.String(
        required=True, error_messages={"required": "article_id is required."}
    )
    title = fields.String(
        required=True, error_messages={"required": "title is required."}
    )
    author_first_name = fields.String(
        required=True, error_messages={"required": "author_first_name is required."}
    )
    author_last_name = fields.String(
        required=True, error_messages={"required": "author_last_name is required."}
    )


# Validate article
def article_validate(article_payload):
    ArticleSchema().load(article_payload)


# Validate list of article - just some fields
def list_articles_validate(list_articles_payload):
    ListArticlesSchema().load(list_articles_payload)
