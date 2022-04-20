from flask import Blueprint, render_template
from app.controllers import articles
from app.api.api_models import ArticleListApiModel

page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
def home():
    return render_template("page/home.html")


@page.route("/blogs")
def blogs():
    list_articles: ArticleListApiModel = articles()
    blogs = [
        (t.article_id, t.title, t.author_first_name, t.author_last_name)
        for t in list_articles
    ]
    return render_template("page/list_blogs.html", blogs=blogs)
