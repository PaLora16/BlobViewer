from tortoise.models import Model
from tortoise import fields


class Article(Model):
    id = fields.IntField(pk=True)
    article_id = fields.TextField()
    title = fields.TextField()
    content = fields.TextField()
    created_at = fields.DatetimeField()
    comments_number = fields.IntField()
    author_first_name = fields.TextField()
    author_last_name = fields.TextField()
    
    class Meta:
        table = "Article"

    def __str__(self):
        return self.title
